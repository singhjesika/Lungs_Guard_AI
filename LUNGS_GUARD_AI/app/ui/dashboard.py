import streamlit as st
import pandas as pd

from app.ui.theme import inject_css, animated_lung, glass_card_start, glass_card_end, risk_pill

st.set_page_config(page_title="LungsGuard AI", page_icon="🫁", layout="wide")

if not st.session_state.get("logged_in"):
    from app.ui.login_page import render as render_login
    render_login()
    st.stop()

inject_css()

with st.sidebar:
    st.markdown('<div class="glow-title" style="font-size:1.6rem;">🫁 LungsGuard AI</div>', unsafe_allow_html=True)
    st.markdown(f"**Patient:** {st.session_state.get('patient_name','—')}  \n**Age:** {st.session_state.get('patient_age','—')}")
    st.divider()
    page = st.radio("Navigate", ["Dashboard", "Upload & Predict", "Reports"])
    st.divider()
    if st.button("Log out", use_container_width=True):
        st.session_state.clear()
        st.rerun()

history = st.session_state.get("history", [])

if page == "Dashboard":
    animated_lung()
    st.markdown('<div class="glow-title" style="text-align:center;">LungsGuard AI — Dashboard</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#9CA3AF;'>Overview of your lung health insights</p>", unsafe_allow_html=True)

    if not history:
        glass_card_start()
        st.info("No predictions yet. Go to **Upload & Predict** to run your first assessment.")
        glass_card_end()
    else:
        latest = history[-1]
        score = round((1 - latest["risk_score"]) * 100, 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            glass_card_start()
            st.markdown("**🎯 Lung Health Score**")
            st.markdown(f"<h1 style='margin:0;'>{score}/100</h1>", unsafe_allow_html=True)
            st.progress(int(score))
            glass_card_end()
        with col2:
            glass_card_start()
            st.markdown("**🩺 Latest Risk Level**")
            st.markdown(risk_pill(latest["risk_level"], latest["icon"]), unsafe_allow_html=True)
            st.markdown(f"<h2 style='margin-top:0.5rem;'>{latest['probability']*100:.1f}%</h2>", unsafe_allow_html=True)
            glass_card_end()
        with col3:
            glass_card_start()
            st.markdown("**📊 Total Assessments**")
            st.markdown(f"<h1 style='margin:0;'>{len(history)}</h1>", unsafe_allow_html=True)
            glass_card_end()

        glass_card_start()
        st.markdown("**📈 Health Trend (Risk Probability over time)**")
        df = pd.DataFrame({
            "Assessment #": list(range(1, len(history) + 1)),
            "Risk Probability": [h["probability"] for h in history],
        }).set_index("Assessment #")
        st.line_chart(df, height=260)
        glass_card_end()

        glass_card_start()
        st.markdown("**🤖 Explainability — Last Prediction**")
        explain = latest.get("explanation", {})
        if explain:
            exp_df = pd.DataFrame(
                sorted(explain.items(), key=lambda x: abs(x[1]), reverse=True),
                columns=["Feature", "Impact"]
            ).set_index("Feature")
            st.bar_chart(exp_df, height=260)
            st.caption("Positive values increase predicted risk; negative values decrease it.")
        else:
            st.info("No explainability data available for this prediction.")
        glass_card_end()

elif page == "Upload & Predict":
    from app.ui.upload_page import render
    render()

elif page == "Reports":
    from app.ui.report_page import render
    render()