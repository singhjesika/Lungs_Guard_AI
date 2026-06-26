import streamlit as st

PRIMARY = "#22D3EE"
ACCENT = "#A78BFA"
PINK = "#F472B6"
GREEN = "#34D399"
BG_DARK = "#060B18"


def inject_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    .stApp {{
        font-family: 'Inter', sans-serif;
        background:
            radial-gradient(ellipse at 0% 0%, #0d2137 0%, transparent 55%),
            radial-gradient(ellipse at 100% 0%, #1a0a2e 0%, transparent 55%),
            radial-gradient(ellipse at 50% 100%, #0a1628 0%, transparent 60%),
            linear-gradient(160deg, {BG_DARK} 0%, #080d1a 50%, #060a14 100%);
        color: #E5E7EB;
        min-height: 100vh;
    }}

    .stApp::before {{
        content: '';
        position: fixed;
        top: -40%;
        left: -10%;
        width: 55%;
        height: 80%;
        background: radial-gradient(ellipse, rgba(34,211,238,0.07) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }}

    .stApp::after {{
        content: '';
        position: fixed;
        bottom: -30%;
        right: -10%;
        width: 55%;
        height: 80%;
        background: radial-gradient(ellipse, rgba(167,139,250,0.07) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, rgba(10,16,35,0.98) 0%, rgba(8,12,28,0.98) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(34,211,238,0.12);
        box-shadow: 4px 0 24px rgba(0,0,0,0.4);
    }}

    .glass-card {{
        background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
        border: 1px solid rgba(34,211,238,0.15);
        border-radius: 20px;
        padding: 1.4rem 1.6rem;
        backdrop-filter: blur(16px);
        box-shadow:
            0 8px 32px rgba(0,0,0,0.4),
            0 0 0 1px rgba(255,255,255,0.03),
            inset 0 1px 0 rgba(255,255,255,0.06);
        margin-bottom: 1.2rem;
        position: relative;
        overflow: hidden;
    }}

    .glass-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(34,211,238,0.4), transparent);
    }}

    .glow-title {{
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, {PRIMARY} 0%, {ACCENT} 50%, {PINK} 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 0.3rem;
        letter-spacing: -0.5px;
        text-shadow: none;
        filter: drop-shadow(0 0 20px rgba(34,211,238,0.3));
    }}

    .pill {{
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 700;
        margin-right: 0.4rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}

    .lung-wrap {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1.2rem 0 0.6rem 0;
        position: relative;
    }}

    .lung-wrap::before {{
        content: '';
        position: absolute;
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(34,211,238,0.12) 0%, transparent 70%);
        animation: pulse-ring 3.2s ease-in-out infinite;
    }}

    .lung {{
        font-size: 5rem;
        animation: breathe 3.2s ease-in-out infinite;
        filter: drop-shadow(0 0 18px {PRIMARY}) drop-shadow(0 0 40px rgba(34,211,238,0.3));
        position: relative;
        z-index: 1;
    }}

    @keyframes breathe {{
        0%   {{ transform: scale(0.90); filter: drop-shadow(0 0 10px {PRIMARY}) drop-shadow(0 0 30px rgba(34,211,238,0.2)); }}
        50%  {{ transform: scale(1.10); filter: drop-shadow(0 0 30px {PRIMARY}) drop-shadow(0 0 60px rgba(167,139,250,0.4)); }}
        100% {{ transform: scale(0.90); filter: drop-shadow(0 0 10px {PRIMARY}) drop-shadow(0 0 30px rgba(34,211,238,0.2)); }}
    }}

    @keyframes pulse-ring {{
        0%   {{ transform: scale(0.9); opacity: 0.6; }}
        50%  {{ transform: scale(1.2); opacity: 0.2; }}
        100% {{ transform: scale(0.9); opacity: 0.6; }}
    }}

    .stButton > button {{
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT});
        color: #060B18;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        font-family: 'Inter', sans-serif;
        padding: 0.6rem 1.6rem;
        transition: all 0.25s ease;
        box-shadow: 0 4px 20px rgba(34,211,238,0.25);
        letter-spacing: 0.3px;
    }}

    .stButton > button:hover {{
        filter: brightness(1.12);
        transform: translateY(-2px);
        box-shadow: 0 8px 28px rgba(34,211,238,0.4);
    }}

    div[data-testid="stMetric"] {{
        background: linear-gradient(135deg, rgba(34,211,238,0.08) 0%, rgba(167,139,250,0.05) 100%);
        border: 1px solid rgba(34,211,238,0.18);
        border-radius: 16px;
        padding: 0.8rem 1rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.05);
    }}

    div[data-testid="stMetric"] label {{
        color: {PRIMARY} !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        letter-spacing: 0.5px;
    }}

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }}

    .stSelectbox > div, .stSlider > div {{
        background: rgba(255,255,255,0.03) !important;
    }}

    .stTextInput > div > div > input {{
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(34,211,238,0.2) !important;
        border-radius: 12px !important;
        color: #E5E7EB !important;
    }}

    .stTextInput > div > div > input:focus {{
        border-color: {PRIMARY} !important;
        box-shadow: 0 0 0 2px rgba(34,211,238,0.15) !important;
    }}

    .stProgress > div > div > div {{
        background: linear-gradient(90deg, {PRIMARY}, {ACCENT}) !important;
        border-radius: 999px !important;
    }}

    .stProgress > div > div {{
        background: rgba(255,255,255,0.06) !important;
        border-radius: 999px !important;
    }}

    .stAlert {{
        background: rgba(34,211,238,0.08) !important;
        border: 1px solid rgba(34,211,238,0.2) !important;
        border-radius: 14px !important;
        color: #E5E7EB !important;
    }}

    h1, h2, h3 {{
        color: #F1F5F9 !important;
        font-family: 'Inter', sans-serif !important;
    }}

    .stRadio > label {{
        color: #94A3B8 !important;
        font-size: 0.78rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        font-weight: 600 !important;
    }}

    .stRadio > div > label {{
        color: #CBD5E1 !important;
        font-size: 0.95rem !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        font-weight: 500 !important;
    }}

    hr {{
        border-color: rgba(34,211,238,0.12) !important;
    }}

    ::-webkit-scrollbar {{
        width: 5px;
    }}
    ::-webkit-scrollbar-track {{
        background: rgba(255,255,255,0.02);
    }}
    ::-webkit-scrollbar-thumb {{
        background: rgba(34,211,238,0.25);
        border-radius: 999px;
    }}
    </style>
    """, unsafe_allow_html=True)


def animated_lung():
    st.markdown('<div class="lung-wrap"><div class="lung">🫁</div></div>', unsafe_allow_html=True)


def glass_card_start():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)


def glass_card_end():
    st.markdown('</div>', unsafe_allow_html=True)


def risk_pill(level: str, icon: str) -> str:
    colors = {
        "CRITICAL": "#EF4444",
        "HIGH": "#F97316",
        "MODERATE": "#FACC15",
        "LOW": "#22C55E",
    }
    color = colors.get(level, "#9CA3AF")
    return f'<span class="pill" style="background:{color}18; color:{color}; border:1px solid {color}55; box-shadow: 0 0 12px {color}33;">{icon} {level}</span>'