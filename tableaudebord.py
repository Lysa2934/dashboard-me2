"""
DASHBOARD - MEL Plan (Monitoring, Evaluation & Learning)
Project: Reduction in Trade-Related Gender Discrimination
in West Africa

How to run this dashboard:
1. Open a terminal
2. Install the required libraries (only once):
   py -m pip install streamlit pandas
3. Run the dashboard:
   streamlit run tableaudebord.py
"""

import streamlit as st
import pandas as pd

# ------------------------------------------------------------------
# PAGE SETTINGS
# ------------------------------------------------------------------
st.set_page_config(
    page_title="MEL Dashboard - Gender & Trade",
    page_icon="📊",
    layout="wide",
)

# ------------------------------------------------------------------
# PROJECT DATA (extracted from the Word document)
# ------------------------------------------------------------------

# List of indicators from the Results Framework
# baseline: starting value (None if "TBD" = to be determined)
# target: value to reach by end of project
# unit: "number" or "%"
indicators = [
    dict(level="IMPACT", indicator="Reduction in gender-based discrimination reported by women CBTs",
         baseline=None, target=40, unit="% reduction", frequency="Annual", responsible="AITCR/TMA"),

    dict(level="OUTCOME 1 - Capacity & Institutional Reform",
         indicator="% of targeted border officers demonstrating gender-responsive behavior",
         baseline=0, target=70, unit="%", frequency="Quarterly", responsible="AITCR/ACINTaD/AFRIK'ACT"),
    dict(level="OUTCOME 1 - Capacity & Institutional Reform",
         indicator="Number of border officials trained (ToT cascade)",
         baseline=0, target=120, unit="number", frequency="Per training event", responsible="AITCR"),
    dict(level="OUTCOME 1 - Capacity & Institutional Reform",
         indicator="Number of gender-responsive SOPs adopted",
         baseline=0, target=6, unit="number", frequency="Semi-annual", responsible="ACINTaD/AFRIK'ACT"),
    dict(level="OUTCOME 1 - Capacity & Institutional Reform",
         indicator="Number of Gender Champion Networks operational",
         baseline=0, target=6, unit="number", frequency="Quarterly", responsible="AFRIK'ACT/ACINTaD"),

    dict(level="OUTCOME 2 - Reporting Mechanisms & Dialogue",
         indicator="Number of safe, operational reporting mechanisms",
         baseline=0, target=6, unit="number", frequency="Semi-annual", responsible="AITCR"),
    dict(level="OUTCOME 2 - Reporting Mechanisms & Dialogue",
         indicator="Number of CBTs sensitized on reporting mechanisms",
         baseline=0, target=2700, unit="number", frequency="Per event", responsible="ACINTaD/AFRIK'ACT"),
    dict(level="OUTCOME 2 - Reporting Mechanisms & Dialogue",
         indicator="% of reported incidents receiving a documented response within 30 days",
         baseline=None, target=80, unit="%", frequency="Quarterly", responsible="AITCR"),
    dict(level="OUTCOME 2 - Reporting Mechanisms & Dialogue",
         indicator="Number of Corridor Gender & Trade Barometers published",
         baseline=0, target=3, unit="number", frequency="Annual", responsible="AITCR"),
    dict(level="OUTCOME 2 - Reporting Mechanisms & Dialogue",
         indicator="Number of quarterly border-level dialogues held",
         baseline=0, target=24, unit="number", frequency="Quarterly", responsible="All partners"),

    dict(level="OUTCOME 3 - Inclusive Micro-Infrastructure",
         indicator="Number of gender-sensitive micro-infrastructure sites rehabilitated",
         baseline=0, target=3, unit="number", frequency="At completion", responsible="AFRIK'ACT/ACINTaD"),
    dict(level="OUTCOME 3 - Inclusive Micro-Infrastructure",
         indicator="% of women CBTs reporting improved perceived safety",
         baseline=None, target=60, unit="%", frequency="Annual", responsible="AITCR"),
    dict(level="OUTCOME 3 - Inclusive Micro-Infrastructure",
         indicator="% of rehabilitated sites with women-led O&M systems",
         baseline=0, target=100, unit="%", frequency="6 months after handover", responsible="AFRIK'ACT/ACINTaD"),

    dict(level="CROSS-CUTTING - Knowledge & Awareness",
         indicator="Number of CBTs who received trade and gender rights information",
         baseline=0, target=4800, unit="number", frequency="Per event", responsible="All partners"),
    dict(level="CROSS-CUTTING - Knowledge & Awareness",
         indicator="Number of QR-code linked knowledge materials deployed",
         baseline=0, target=6, unit="number", frequency="Semi-annual", responsible="AITCR/AFRIK'ACT"),
    dict(level="CROSS-CUTTING - Knowledge & Awareness",
         indicator="% of women CBTs reporting increased knowledge of rights",
         baseline=None, target=60, unit="%", frequency="Annual", responsible="AITCR"),
    dict(level="CROSS-CUTTING - Knowledge & Awareness",
         indicator="Number of informational videos produced and viewed",
         baseline=0, target=6, unit="number", frequency="Semi-annual", responsible="AFRIK'ACT"),
]
df_indicators = pd.DataFrame(indicators)

# MEL risk register
risks = [
    dict(risk="Under-reporting of GBV/incidents due to stigma or fear",
         likelihood="High", impact="High", rating="Severe"),
    dict(risk="Inconsistent or missing data from field teams across 6 countries",
         likelihood="Medium", impact="High", rating="High"),
    dict(risk="Data privacy breach of sensitive incident records",
         likelihood="Medium", impact="High", rating="High"),
    dict(risk="Staff turnover interrupting data continuity",
         likelihood="Medium", impact="Medium", rating="Moderate"),
    dict(risk="Security incidents preventing field data collection",
         likelihood="Medium", impact="Medium", rating="Moderate"),
    dict(risk="Response bias in trader self-reports",
         likelihood="Medium", impact="Medium", rating="Moderate"),
]
df_risks = pd.DataFrame(risks)

# Reporting calendar
calendar = [
    dict(report="Monthly Activity Flash Report", frequency="Monthly", deadline="5th of following month"),
    dict(report="Quarterly Progress & Financial Report", frequency="Quarterly", deadline="15th after quarter end"),
    dict(report="Quarterly Learning Note", frequency="Quarterly", deadline="With Quarterly Progress Report"),
    dict(report="Mid-Term Review Report", frequency="Once (Month 18-20)", deadline="End of Month 20"),
    dict(report="Annual Corridor Gender & Trade Barometer", frequency="Annual", deadline="December each year"),
    dict(report="Success Stories / Case Studies", frequency="Semi-annual", deadline="June & December"),
    dict(report="Final Evaluation Report", frequency="Once (Month 35)", deadline="End of Month 35"),
    dict(report="End-of-Project Report", frequency="Once (Month 36)", deadline="End of Month 36"),
]
df_calendar = pd.DataFrame(calendar)

# ------------------------------------------------------------------
# SIDEBAR SETTINGS (font, size, colors)
# ------------------------------------------------------------------
# Everything the user picks here is turned into a small block of CSS
# below and injected into the page with st.markdown().
with st.sidebar:
    st.header("⚙️ Display settings")

    font_choice = st.selectbox(
        "Font",
        ["Arial", "Georgia", "Verdana", "Courier New", "Trebuchet MS"],
    )

    font_size = st.slider(
        "Text size (px)",
        min_value=12, max_value=24, value=16, step=1,
    )

    theme_choice = st.selectbox(
        "Color theme",
        ["Blue (default)", "Green", "Purple", "Orange", "Dark"],
    )

# Each theme = one accent color + one background color
themes = {
    "Blue (default)": dict(accent="#1F4E5F", background="#FFFFFF"),
    "Green":           dict(accent="#1E5631", background="#F4FAF6"),
    "Purple":          dict(accent="#4B2E83", background="#F8F5FC"),
    "Orange":          dict(accent="#B85C00", background="#FFF8F0"),
    "Dark":            dict(accent="#F0F0F0", background="#1E1E1E"),
}
accent = themes[theme_choice]["accent"]
background = themes[theme_choice]["background"]
text_color = "#F0F0F0" if theme_choice == "Dark" else "#111111"

# Build the CSS block from the user's choices and inject it into the page.
custom_css = f"""
<style>
    html, body, [class*="css"] {{
        font-family: '{font_choice}', sans-serif;
        font-size: {font_size}px;
        color: {text_color};
    }}
    .stApp {{
        background-color: {background};
    }}
    h1, h2, h3 {{
        color: {accent} !important;
    }}
    .stButton>button, .stTabs [aria-selected="true"] {{
        color: {accent} !important;
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------
st.title("📊 MEL Plan Dashboard")
st.subheader("Reduction in Trade-Related Gender Discrimination - West Africa")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Programme duration", "36 months")
col2.metric("Countries covered", "6")
col3.metric("Corridors", "2")
col4.metric("Indicators tracked", len(df_indicators))

st.caption("Corridors: Abidjan–Lagos | Tema–Ouagadougou. "
           "Countries: Benin, Burkina Faso, Côte d'Ivoire, Ghana, Nigeria, Togo. "
           "Financed by TradeMark Africa (TMA).")

st.divider()

# ------------------------------------------------------------------
# TABS
# ------------------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🎯 Indicators", "⚠️ Risks", "📅 Reporting Calendar"])

# ---------- TAB 1: INDICATORS ----------
with tab1:
    st.write("Select a result level to filter, then enter the current value "
             "for each indicator to track progress toward the target.")

    levels = ["All"] + sorted(df_indicators["level"].unique().tolist())
    chosen_level = st.selectbox("Filter by result level:", levels)

    if chosen_level == "All":
        filtered_table = df_indicators
    else:
        filtered_table = df_indicators[df_indicators["level"] == chosen_level]

    st.write(f"**{len(filtered_table)} indicator(s) displayed**")

    for i, row in filtered_table.iterrows():
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"**{row['indicator']}**")
                st.caption(f"{row['level']} • Frequency: {row['frequency']} • Responsible: {row['responsible']}")
            with c2:
                baseline_txt = "To be determined" if row["baseline"] is None else str(row["baseline"])
                st.write(f"Baseline: {baseline_txt}")
                st.write(f"Target: {row['target']} ({row['unit']})")

            current_value = st.number_input(
                "Current value",
                min_value=0,
                value=0,
                key=f"value_{i}",
                label_visibility="collapsed",
            )
            target = row["target"]
            progress = min(current_value / target, 1.0) if target else 0
            st.progress(progress, text=f"{progress*100:.0f}% of target reached")

# ---------- TAB 2: RISKS ----------
with tab2:
    st.write("Register of risks specific to monitoring and evaluation (MEL), with their severity level.")

    def rating_color(rating):
        colors = {"Severe": "background-color: #f8d7da",
                  "High": "background-color: #fff3cd",
                  "Moderate": "background-color: #d1e7dd"}
        return colors.get(rating, "")

    st.dataframe(
        df_risks.style.applymap(lambda v: rating_color(v), subset=["rating"]),
        use_container_width=True,
        hide_index=True,
    )

    st.write("Breakdown of risks by severity level:")
    breakdown = df_risks["rating"].value_counts()
    st.bar_chart(breakdown)

# ---------- TAB 3: CALENDAR ----------
with tab3:
    st.write("Consolidated reporting schedule for the full 36-month programme.")
    st.dataframe(df_calendar, use_container_width=True, hide_index=True)

st.divider()
st.caption("Dashboard generated from the MEL Plan. Values entered in 'Current value' "
           "are not saved automatically — remember to note them down elsewhere if needed.")
