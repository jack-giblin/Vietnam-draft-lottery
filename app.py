import streamlit as st
from draft_data import DRAFT_LOTTERY_1969, DRAFT_LOTTERY_1970, DRAFT_LOTTERY_1971, DRAFT_LOTTERY_1972
from story_generator import generate_draft_story
from datetime import datetime

# Page config
st.set_page_config(
    page_title="The Lottery — Vietnam Draft Checker",
    page_icon="🎖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-block">
    <div class="header-stamp">CLASSIFIED</div>
    <h1 class="title">THE LOTTERY</h1>
    <p class="subtitle">Vietnam Era Draft Checker · 1969–1972</p>
    <p class="tagline">Enter your birthday. Find out if your number came up.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Input ────────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">YOUR DATE OF BIRTH</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    month = st.selectbox(
        "Month",
        options=list(range(1, 13)),
        format_func=lambda m: datetime(2000, m, 1).strftime("%B"),
        index=0,
        key="month_select"
    )
with col2:
    # Days in each month (non-leap)
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = st.selectbox(
        "Day",
        options=list(range(1, days_in_month[month - 1] + 1)),
        index=0,
        key="day_select"
    )

st.markdown('<p class="section-label" style="margin-top:1.5rem">DRAFT YEAR</p>', unsafe_allow_html=True)
year = st.select_slider(
    "Select the lottery year",
    options=[1969, 1970, 1971, 1972],
    value=1969,
    key="year_slider"
)

st.markdown(f"""
<div class="year-note">
Lottery held <b>December {1969 if year == 1968 else year + 1}</b> · 
Affected men born in <b>{year - 26}–{year - 18}</b>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Submit ───────────────────────────────────────────────────────────────────
check = st.button("CHECK YOUR NUMBER", use_container_width=True, key="check_btn")

# ── Results ──────────────────────────────────────────────────────────────────
if check:
    lottery_tables = {
        1969: DRAFT_LOTTERY_1969,
        1970: DRAFT_LOTTERY_1970,
        1971: DRAFT_LOTTERY_1971,
        1972: DRAFT_LOTTERY_1972,
    }

    table = lottery_tables[year]
    date_key = f"{month:02d}-{day:02d}"
    draft_number = table.get(date_key)

    if draft_number is None:
        st.error("Date not found in lottery records. Please check your input.")
    else:
        # Determine status
        thresholds = {1969: 195, 1970: 195, 1971: 125, 1972: 95}
        called_threshold = thresholds[year]
        was_drafted = draft_number <= called_threshold

        status_class = "drafted" if was_drafted else "safe"
        status_label = "DRAFTED" if was_drafted else "NOT CALLED"
        status_icon = "⚠" if was_drafted else "✓"

        month_name = datetime(2000, month, 1).strftime("%B")

        st.markdown(f"""
<div class="result-card {status_class}">
    <div class="result-top">
        <div>
            <div class="result-date">{month_name} {day}</div>
            <div class="result-year">Lottery Year {year}</div>
        </div>
        <div class="result-number-block">
            <div class="result-number-label">LOTTERY NUMBER</div>
            <div class="result-number">{draft_number}</div>
        </div>
    </div>
    <div class="result-status {status_class}">
        <span class="status-icon">{status_icon}</span>
        <span class="status-text">{status_label}</span>
    </div>
    <div class="threshold-note">
        Numbers <b>1–{called_threshold}</b> were called in the {year} lottery
    </div>
</div>
""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Story
        story = generate_draft_story(month, day, year, draft_number, was_drafted)

        st.markdown('<p class="section-label">YOUR STORY</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="story-block">{story}</div>', unsafe_allow_html=True)

        # Footer context
        st.markdown("""
<div class="context-block">
    <p class="context-title">ABOUT THE LOTTERY</p>
    <p class="context-text">
        The Vietnam draft lottery was introduced on December 1, 1969 — the first U.S. draft lottery since 
        World War II. Each day of the year was assigned a random number from 1 to 366. 
        Men turning 19 that year were subject to induction based on their lottery number. 
        Those with lower numbers were called first; many never came home.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="page-footer">
    <p>Built for historical education. Data sourced from official Selective Service records.</p>
    <p>In memory of the 58,220 Americans who gave their lives in Vietnam.</p>
</div>
""", unsafe_allow_html=True)
