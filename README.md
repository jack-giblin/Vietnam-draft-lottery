# The Lottery — Vietnam Draft Checker

A historically grounded web app that lets you enter any birthday (month/day) and discover what your Vietnam War draft lottery number would have been — and the story that might have followed.

Built with Streamlit. Designed with a Vietnam-era aesthetic: typewriter fonts, parchment tones, and honest narrative prose.

---

## Features

- **Four lottery years**: 1969, 1970, 1971, 1972 — all sourced from official Selective Service records
- **Real draft numbers**: Every birthday maps to its actual historical lottery number
- **Personalized stories**: Whether drafted or spared, you get a narrative grounded in real units, real locations, and real history
- **Clean, thematic design**: Parchment palette, typewriter fonts, no clutter

---

## Project Structure

```
vietnam_draft/
├── app.py              # Main Streamlit application
├── draft_data.py       # All four lottery tables (1969–1972)
├── story_generator.py  # Narrative engine
├── style.css           # Vietnam-era CSS theme
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/vietnam-draft-checker.git
cd vietnam-draft-checker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## Deploying to Streamlit Community Cloud

1. Push this repo to GitHub (public or private)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"**
4. Select your repository, branch (`main`), and set **Main file path** to `app.py`
5. Click **Deploy**

Streamlit Community Cloud is free for public apps and handles all hosting automatically.

---

## Data Sources

Draft lottery numbers sourced from:
- U.S. Selective Service System official records
- National Archives: *Records of the Selective Service System, RG 147*
- Congressional Research Service historical reports on the Vietnam draft

---

## Historical Context

The Vietnam draft lottery was first held on **December 1, 1969** — the first U.S. lottery draft since World War II. Each day of the year was randomly assigned a number from 1 to 366. Men whose birthdays fell within the called range received induction notices.

| Lottery Year | Numbers Called | Men Affected |
|---|---|---|
| 1969 | 1–195 | Born 1944–1950 |
| 1970 | 1–195 | Born 1944–1950 |
| 1971 | 1–125 | Born 1951 |
| 1972 | 1–95  | Born 1952 |

**58,220 Americans** were killed in Vietnam. This app is built in their memory.

---

*For historical education only.*
