"""
Feature-verkenner – hommelgeluiden (Datalab 3)

Laat zien welke features de gedragsklassen (buzz, flight, noise, radio, voice) het best onderscheiden,
met uitleg per feature en per methode.

Starten (vanuit de projectmap):
    pip install streamlit plotly scikit-learn pandas
    streamlit run feature_app.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import f_classif, mutual_info_classif

st.set_page_config(page_title="Feature-verkenner hommelgeluiden", page_icon="🐝", layout="wide")

KLASSEN = ["buzz", "flight", "noise", "radio", "voice"]
KLEUR = {"buzz": "#2a78d6", "flight": "#eb6834", "noise": "#1baf7a", "radio": "#eda100", "voice": "#e87ba4"}
TYPE_KLEUR = {"MFCC-gemiddelde": "#2a78d6", "MFCC-spreiding": "#7fb2ec", "Delta (verandering)": "#1baf7a",
              "Spectraal / energie": "#eb6834"}
RECORDER_KLEUR = {"16 kHz": "#898781", "384 kHz": "#4a3aa7"}
TEKST = ["start", "end", "label", "source_file"]
SEED = 42

KANDIDATEN = [
    "data/processed_data/bee_features_per_second.csv",
    "../data/processed_data/bee_features_per_second.csv",
    "bee_features_per_second.csv",
]


# ---------------------------------------------------------------- uitleg per feature
def feature_type(f):
    if f.startswith("mfcc_") and f.endswith("_mean"):
        return "MFCC-gemiddelde"
    if f.startswith("mfcc_") and f.endswith("_std"):
        return "MFCC-spreiding"
    if f.startswith("delta_"):
        return "Delta (verandering)"
    return "Spectraal / energie"


VASTE_UITLEG = {
    "rms_mean": "**Energie / luidheid.** Het gemiddelde vermogen van het signaal in deze seconde. Hoog bij stemmen en harde geluiden dicht bij de microfoon.",
    "zcr_mean": "**Zero-crossing rate.** Hoe vaak het signaal per sample door nul gaat. Hoog bij ruisachtig of hoogfrequent geluid. Hangt sterk samen met de spectral centroid.",
    "spectral_centroid_mean": "**Helderheid (Hz).** Het zwaartepunt van het spectrum: waar de energie gemiddeld ligt. Een hogere waarde klinkt 'scherper'. Let op: verschilt sterk tussen de twee recorders.",
    "spectral_rolloff_mean": "**Rolloff (Hz).** De frequentie waaronder 85% van de energie ligt. Meet bijna hetzelfde als de centroid (r ≈ 0,95).",
}


def uitleg(f):
    if f in VASTE_UITLEG:
        return VASTE_UITLEG[f]
    n = int(f.split("_")[1])
    if f.startswith("delta_"):
        return (f"**Delta van MFCC {n}.** Hoe snel coëfficiënt {n} verandert binnen de seconde. "
                "Hoog bij plotselinge overgangen (een geluid dat begint of stopt), laag bij een constant geluid.")
    soort = "gemiddelde" if f.endswith("_mean") else "spreiding (standaarddeviatie)"
    if n == 1:
        wat = "MFCC 1 beschrijft vooral de **totale energie** van het geluid."
    elif n == 2:
        wat = "MFCC 2 beschrijft de **balans tussen lage en hoge tonen**; beweegt tegengesteld aan de spectral centroid."
    elif n <= 10:
        wat = (f"MFCC {n} beschrijft de **grove vorm van het spectrum** (de klankkleur). "
               "In de EDA verschillen de klassen vooral bij MFCC 2–10.")
    else:
        wat = (f"MFCC {n} beschrijft **fijne details** in het spectrum. "
               "In de EDA liggen de klassen bij MFCC 11–20 dicht bij elkaar.")
    extra = "" if soort == "gemiddelde" else " De spreiding zegt hoe stabiel die klankkleur is binnen de seconde."
    return f"**MFCC {n}, {soort}.** {wat}{extra}"


# ---------------------------------------------------------------- data
@st.cache_data(show_spinner="Data laden …")
def laad(pad):
    df = pd.read_csv(pad, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    for k in TEKST:
        df[k] = df[k].astype("string").str.strip()
    df = df.drop_duplicates().reset_index(drop=True)
    datum = pd.to_datetime(df["start"]).dt.strftime("%Y-%m-%d")
    # 16 kHz-opnames zijn allemaal van 26 mei, de 384 kHz-opnames van maart/april (zie EDA 3.5)
    df["recorder"] = np.where(datum == "2026-05-26", "16 kHz", "384 kHz")
    features = [k for k in df.columns if k not in TEKST + ["recorder"]]
    lab = df.dropna(subset=["label"]).copy()
    lab["label"] = lab["label"].astype(str)
    return lab, features


@st.cache_data(show_spinner="Scores berekenen …")
def bereken_scores(lab, features, alleen16):
    data = lab[lab["recorder"] == "16 kHz"] if alleen16 else lab
    X, y = data[features], data["label"]
    F, p = f_classif(X, y)
    mi = mutual_info_classif(X, y, random_state=SEED)
    rf = RandomForestClassifier(n_estimators=300, class_weight="balanced", n_jobs=-1, random_state=SEED).fit(X, y)
    F_rec, _ = f_classif(lab[features], lab["recorder"]) if lab["recorder"].nunique() > 1 else (np.zeros(len(features)), None)
    s = pd.DataFrame({"ANOVA F": F, "p-waarde": p, "Mutual information": mi,
                      "Random Forest": rf.feature_importances_, "F recorder": F_rec}, index=features)
    rang = s[["ANOVA F", "Mutual information", "Random Forest"]].rank(ascending=False)
    s["Gecombineerd"] = -rang.mean(axis=1)  # hoger = beter
    s["gemiddelde rang"] = rang.mean(axis=1)
    s["recorder-rang"] = s["F recorder"].rank(ascending=False).astype(int)
    s["type"] = [feature_type(f) for f in features]
    return s.sort_values("gemiddelde rang"), len(data)


def verwijder_dubbel(volgorde, corr, drempel):
    gekozen, weg = [], {}
    for f in volgorde:
        m = [g for g in gekozen if corr.loc[f, g] > drempel]
        if m:
            weg[f] = m[0]
        else:
            gekozen.append(f)
    return gekozen, weg


# ---------------------------------------------------------------- zijbalk
st.sidebar.title("🐝 Instellingen")
standaard = next((k for k in KANDIDATEN if Path(k).exists()), KANDIDATEN[0])
pad = st.sidebar.text_input("Pad naar de feature-CSV", standaard)
if not Path(pad).exists():
    st.error(f"Bestand niet gevonden: `{pad}`. Pas het pad aan in de zijbalk.")
    st.stop()

lab, FEATURES = laad(pad)

dataset = st.sidebar.radio(
    "Welke opnames?", ["Alleen 16 kHz (aanbevolen)", "Alle opnames"],
    help="De twee recorders verschillen sterk. Met alleen 16 kHz telt dat verschil niet mee als 'onderscheidend'.")
alleen16 = dataset.startswith("Alleen")
top_n = st.sidebar.slider("Aantal features in de ranglijst", 5, len(FEATURES), 15)
drempel = st.sidebar.slider("Correlatiedrempel voor dubbele informatie", 0.70, 0.99, 0.85, 0.01)
toon_recorder = st.sidebar.checkbox("Markeer features die vooral de recorder meten", True)

scores, n_rijen = bereken_scores(lab, FEATURES, alleen16)
data = lab[lab["recorder"] == "16 kHz"] if alleen16 else lab
corr = data[FEATURES].corr().abs()
schoon, weg = verwijder_dubbel(scores.index, corr, drempel)
recorder_top = set(scores.nsmallest(10, "recorder-rang").index)

# ---------------------------------------------------------------- kop
st.title("Welke features onderscheiden het gedrag van de hommel?")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Gelabelde seconden", f"{n_rijen:,}".replace(",", "."))
c2.metric("Features", len(FEATURES))
c3.metric("Beste feature", scores.index[0])
c4.metric("Overbodig door correlatie", len(weg))

json_pad = Path(pad).with_name("geselecteerde_features.json")
if json_pad.exists():
    sel = json.loads(json_pad.read_text())
    st.success(f"**Selectie uit het notebook** (top {sel['k']}, macro-F1 {sel['macro_f1_selectie']} "
               f"vs {sel['macro_f1_alle']} met alle features): " + ", ".join(f"`{f}`" for f in sel["features"]))

tab1, tab2, tab3, tab4 = st.tabs(["📊 Ranglijst", "🔍 Per feature", "🔗 Samenhang", "📖 Uitleg"])

# ---------------------------------------------------------------- tab 1
with tab1:
    methode = st.radio("Sorteer op", ["Gecombineerd", "ANOVA F", "Mutual information", "Random Forest"], horizontal=True)
    zonder_dubbel = st.checkbox("Verberg features die dubbele informatie geven", False)
    volgorde = scores.sort_values(methode, ascending=False)
    if zonder_dubbel:
        volgorde = volgorde.loc[[f for f in volgorde.index if f in schoon]]
    top = volgorde.head(top_n).iloc[::-1]
    waarde = top["gemiddelde rang"] if methode == "Gecombineerd" else top[methode]
    labels = [f"{f}  ⚠" if (toon_recorder and f in recorder_top) else f for f in top.index]

    fig = go.Figure()
    for t, kleur in TYPE_KLEUR.items():
        m = top["type"] == t
        if m.any():
            fig.add_bar(y=np.array(labels)[m], x=waarde[m], orientation="h", name=t, marker_color=kleur,
                        hovertemplate="%{y}<br>%{x:.3f}<extra>" + t + "</extra>")
    fig.update_layout(height=max(320, 26 * len(top) + 80), barmode="overlay", margin=dict(l=10, r=10, t=30, b=10),
                      yaxis=dict(categoryorder="array", categoryarray=labels),
                      xaxis_title="gemiddelde rang (lager = beter)" if methode == "Gecombineerd" else methode,
                      legend=dict(orientation="h", y=1.06, x=0))
    if methode == "Gecombineerd":
        fig.update_xaxes(autorange="reversed")
    st.plotly_chart(fig, width="stretch")
    if toon_recorder:
        st.caption("⚠ = hoort bij de 10 features die de twee recorders het sterkst scheiden. "
                   "Zo'n feature kan het model leren *welk apparaat* het was in plaats van *wat de hommel deed*.")

    tabel = volgorde.head(top_n)[["type", "ANOVA F", "p-waarde", "Mutual information", "Random Forest",
                                  "gemiddelde rang", "recorder-rang"]].copy()
    tabel["dubbel met"] = [weg.get(f, "") for f in tabel.index]
    st.dataframe(tabel.style.format({"ANOVA F": "{:.1f}", "p-waarde": "{:.4f}", "Mutual information": "{:.3f}",
                                     "Random Forest": "{:.4f}", "gemiddelde rang": "{:.1f}"}),
                 width="stretch")

# ---------------------------------------------------------------- tab 2
with tab2:
    keuze = st.selectbox("Kies een feature", list(scores.index), index=0)
    links, rechts = st.columns([2, 1])
    with rechts:
        st.markdown(uitleg(keuze))
        r = scores.loc[keuze]
        st.markdown(f"""
| | |
|---|---|
| Gecombineerde rang | **{list(scores.index).index(keuze) + 1}** van {len(scores)} |
| ANOVA F | {r['ANOVA F']:.1f} (p = {r['p-waarde']:.4f}) |
| Mutual information | {r['Mutual information']:.3f} |
| Random Forest | {r['Random Forest']:.4f} |
| Rang als recorder-meter | {r['recorder-rang']} van {len(scores)} |
""")
        if keuze in weg:
            st.warning(f"Geeft grotendeels dezelfde informatie als `{weg[keuze]}` (r = {corr.loc[keuze, weg[keuze]]:.2f}).")
        if keuze in recorder_top:
            st.warning("Deze feature verschilt sterk tussen de twee recorders.")
    with links:
        uitsch = st.checkbox("Toon uitschieters", False)
        kleur_op = "recorder" if not alleen16 else "label"
        fig = px.box(data, x="label", y=keuze, color=kleur_op, category_orders={"label": KLASSEN},
                     color_discrete_map={**KLEUR, **RECORDER_KLEUR}, points="outliers" if uitsch else False)
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=30, b=10), xaxis_title="klasse",
                          showlegend=not alleen16, legend_title="recorder")
        if not uitsch:
            q = data[keuze].quantile([0.01, 0.99])
            fig.update_yaxes(range=[q.iloc[0], q.iloc[1]])
        st.plotly_chart(fig, width="stretch")
        if not alleen16:
            st.caption("Per klasse gesplitst per recorder: liggen de grijze en paarse dozen ver uit elkaar, "
                       "dan meet de feature vooral het verschil tussen de apparaten.")

# ---------------------------------------------------------------- tab 3
with tab3:
    top_f = list(scores.index[:top_n])
    c = data[top_f].corr()
    fig = px.imshow(c, color_continuous_scale=["#2a78d6", "#f0efec", "#e34948"], zmin=-1, zmax=1,
                    aspect="auto", labels=dict(color="r"))
    fig.update_layout(height=max(400, 24 * len(top_f) + 120), margin=dict(l=10, r=10, t=30, b=10))
    st.subheader(f"Correlatie tussen de top {top_n} features")
    st.plotly_chart(fig, width="stretch")
    st.subheader(f"Features die worden overgeslagen (|r| > {drempel:.2f} met een beter scorende feature)")
    if weg:
        st.dataframe(pd.DataFrame({"feature": list(weg), "lijkt op": list(weg.values()),
                                   "r": [round(corr.loc[f, g], 2) for f, g in weg.items()]}),
                     hide_index=True, width="stretch")
    else:
        st.info("Geen paren boven de drempel.")
    st.markdown(f"Na het verwijderen van dubbele informatie blijven er **{len(schoon)}** van de {len(FEATURES)} features over.")

# ---------------------------------------------------------------- tab 4
with tab4:
    st.markdown("""
### Wat zie je in deze app?

Elke rij in de data is **één seconde geluid** met 64 numerieke features. De app rangschikt die features
op hoe goed ze de vijf klassen (`buzz`, `flight`, `noise`, `radio`, `voice`) van elkaar onderscheiden.

### De drie methoden

| Methode | Vraag die hij beantwoordt | Let op |
|---|---|---|
| **ANOVA F** | Verschillen de *gemiddelden* van de klassen veel, vergeleken met de spreiding binnen een klasse? | Ziet alleen verschillen in het gemiddelde, één feature tegelijk |
| **Mutual information** | Hoeveel weet je over de klasse als je deze feature kent? | Ziet ook niet-lineaire verbanden, maar ook één feature tegelijk |
| **Random Forest** | Hoe vaak en hoe nuttig gebruikt een boommodel deze feature? | Gecorreleerde features delen het belang; in de app snel berekend op alle data (het notebook gebruikt de eerlijkere permutation importance per opname) |
| **Gecombineerd** | Gemiddelde rang over de drie methoden | Robuuster dan één methode |

### Waarom alleen 16 kHz?

De dataset heeft opnames van twee recorders (16 kHz en 384 kHz). In de EDA bleek dat het verschil tussen de recorders
groter is dan het verschil tussen de klassen. Met **alle opnames** scoren features als `mfcc_2`, `mfcc_3`, `mfcc_5`
en de spectral centroid hoog, maar vooral omdat ze het apparaat herkennen. Met **alleen 16 kHz** zie je welke
features echt het gedrag onderscheiden.

### Wat zijn MFCC's?

MFCC's (*Mel-frequency cepstral coefficients*) beschrijven de **klankkleur** van een geluid, ongeveer zoals het menselijk oor
die waarneemt. Lage coëfficiënten (1–10) beschrijven de grove vorm van het spectrum, hogere (11–20) de fijne details.
Per seconde is van elke coëfficiënt het **gemiddelde**, de **spreiding** en de **delta** (verandering) opgeslagen.

### Dubbele informatie

Als twee features sterk correleren (|r| boven de drempel), meten ze grotendeels hetzelfde. De app loopt de ranglijst af
en slaat een feature over als hij te veel lijkt op een feature die hoger staat.
""")
