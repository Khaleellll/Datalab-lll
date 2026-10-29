import os
import glob
import numpy as np
import pandas as pd
import librosa
from datetime import datetime, timedelta

# ============================================================
# CONFIG
# ============================================================

RAW_DATA_DIR = os.path.join("data", "raw_data")
LABELS_CSV = os.path.join("data", "raw_labels", "buzzdetection_labels.csv")
OUTPUT_DIR = os.path.join("data", "processed_data")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "bee_features_per_second.csv")

SAMPLE_RATE = 16000

# MFCC settings (applied per 1-second chunk)
N_MFCC = 20
N_FFT = 512
HOP_LENGTH = 256   # ~16ms hop within each 1-second chunk
N_MELS = 64

# ============================================================
# HELPERS
# ============================================================

WAV_FILENAME_FMT = "%Y%m%d_%H%M%S"


def parse_wav_start(filename):
    """Parse recording start datetime from filename like '20260324_111301.WAV'."""
    stem = os.path.splitext(os.path.basename(filename))[0]
    return datetime.strptime(stem, WAV_FILENAME_FMT)


def parse_label_timestamp(ts_str):
    """
    Parse label timestamps like '2026-03-24 11:13:01:00'.
    The trailing ':00' is a sub-second field; we drop it.
    """
    parts = ts_str.rsplit(":", 1)
    return datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")


def load_label_lookup(csv_path):
    """Return a dict mapping datetime (to the second) -> label string."""
    df = pd.read_csv(csv_path)
    lookup = {}
    for _, row in df.iterrows():
        try:
            dt = parse_label_timestamp(str(row["start"]).strip())
            lookup[dt] = str(row["label"]).strip()
        except Exception:
            pass
    return lookup


def extract_second_features(audio_chunk, sr):
    """
    Extract aggregated features from a 1-second audio chunk.
    Returns a flat dict of feature_name -> value (mean across frames).
    """
    if len(audio_chunk) == 0:
        return None

    # Pad if shorter than expected (last chunk of file)
    expected = sr
    if len(audio_chunk) < expected:
        audio_chunk = np.pad(audio_chunk, (0, expected - len(audio_chunk)))

    mfcc = librosa.feature.mfcc(
        y=audio_chunk,
        sr=sr,
        n_mfcc=N_MFCC,
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        n_mels=N_MELS,
    )
    delta = librosa.feature.delta(mfcc)

    zcr = librosa.feature.zero_crossing_rate(audio_chunk, hop_length=HOP_LENGTH)
    rms = librosa.feature.rms(y=audio_chunk, hop_length=HOP_LENGTH)
    spec_centroid = librosa.feature.spectral_centroid(
        y=audio_chunk, sr=sr, n_fft=N_FFT, hop_length=HOP_LENGTH
    )
    spec_rolloff = librosa.feature.spectral_rolloff(
        y=audio_chunk, sr=sr, n_fft=N_FFT, hop_length=HOP_LENGTH
    )

    row = {}
    for j in range(N_MFCC):
        row[f"mfcc_{j+1}_mean"] = float(np.mean(mfcc[j]))
        row[f"mfcc_{j+1}_std"] = float(np.std(mfcc[j]))
        row[f"delta_{j+1}_mean"] = float(np.mean(delta[j]))

    row["zcr_mean"] = float(np.mean(zcr))
    row["rms_mean"] = float(np.mean(rms))
    row["spectral_centroid_mean"] = float(np.mean(spec_centroid))
    row["spectral_rolloff_mean"] = float(np.mean(spec_rolloff))

    return row


# ============================================================
# MAIN
# ============================================================


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    label_lookup = load_label_lookup(LABELS_CSV)
    print(f"Loaded {len(label_lookup)} labeled seconds from {LABELS_CSV}")

    wav_files = sorted(glob.glob(os.path.join(RAW_DATA_DIR, "*.WAV")))
    wav_files += sorted(glob.glob(os.path.join(RAW_DATA_DIR, "*.wav")))

    if not wav_files:
        print(f"No WAV files found in {RAW_DATA_DIR}")
        return

    all_rows = []

    for wav_path in wav_files:
        try:
            file_start = parse_wav_start(wav_path)
        except ValueError:
            print(f"  Skipping {wav_path}: filename doesn't match YYYYMMDD_HHMMSS")
            continue

        print(f"Processing {os.path.basename(wav_path)} (start: {file_start})")

        y, sr = librosa.load(wav_path, sr=SAMPLE_RATE, mono=True)
        duration_seconds = int(np.floor(len(y) / sr))

        for i in range(duration_seconds):
            chunk_start = file_start + timedelta(seconds=i)
            chunk_end = chunk_start + timedelta(seconds=1)

            label = label_lookup.get(chunk_start, None)

            chunk = y[i * sr : (i + 1) * sr]
            features = extract_second_features(chunk, sr)
            if features is None:
                continue

            row = {
                "start": chunk_start.strftime("%Y-%m-%d %H:%M:%S"),
                "end": chunk_end.strftime("%Y-%m-%d %H:%M:%S"),
                "label": label,
                "source_file": os.path.basename(wav_path),
            }
            row.update(features)
            all_rows.append(row)

    if not all_rows:
        print("No rows produced.")
        return

    df = pd.DataFrame(all_rows)
    df.to_csv(OUTPUT_CSV, index=False)

    labeled = df["label"].notna().sum()
    print(f"\nDone. Saved to: {OUTPUT_CSV}")
    print(f"Total rows: {len(df)}  |  Labeled: {labeled}  |  Unlabeled: {len(df) - labeled}")
    print(f"Columns: {df.shape[1]}")


if __name__ == "__main__":
    main()
