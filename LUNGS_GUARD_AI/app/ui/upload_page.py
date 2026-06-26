import streamlit as st
import pandas as pd
import requests

from app.ui.theme import glass_card_start, glass_card_end, risk_pill

API_URL = "http://localhost:8000/api/predict/symptoms"

FEATURES = [
    "gender", "age", "smoking", "yellow_fingers", "anxiety",
    "peer_pressure", "chronic_disease", "fatigue", "allergy",
    "wheezing", "alcohol_consuming", "coughing",
    "shortness_of_breath", "swallowing_difficulty", "chest_pain",
]


def render():
    st.markdown('<div class="glow-title">🔍 Predict Lung Cancer Risk</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#9CA3AF;'>Answer the questions below — your AI model will assess your risk instantly.</p>", unsafe_allow_html=True)

    glass_card_start()
    st.subheader("Symptom Questionnaire")
    inputs = {}
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, feat in enumerate(FEATURES):
        with cols[i % 3]:
            if feat == "age":
                inputs[feat] = st.slider("Age", 20, 90, st.session_state.get("patient_age", 50))
            elif feat == "gender":
                inputs[feat] = st.selectbox("Gender", [0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
            else:
                inputs[feat] = st.selectbox(feat.replace("_", " ").title(), [1, 2], format_func=lambda x: "No" if x == 1 else "Yes")

    predict_clicked = st.button("🚀 Predict Risk", use_container_width=True)
    glass_card_end()

    if predict_clicked:
        try:
            r = requests.post(API_URL, json=inputs, timeout=10)
            result = r.json()

            from app.services.symptom_service import get_feature_importance
            explanation = get_feature_importance(inputs)
            result["explanation"] = explanation

            history = st.session_state.setdefault("history", [])
            history.append(result)

            score = round((1 - result["risk_score"]) * 100, 1)

            glass_card_start()
            st.subheader("Result")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(risk_pill(result["risk_level"], result["icon"]), unsafe_allow_html=True)
                st.markdown(f"<h2 style='margin-top:0.4rem;'>{result['label']}</h2>", unsafe_allow_html=True)
            with c2:
                st.metric("Probability", f"{result['probability']*100:.1f}%")
            with c3:
                st.metric("Lung Health Score", f"{score}/100")
            st.progress(int(score))
            glass_card_end()

            glass_card_start()
            st.markdown("**🤖 Why this result? (Explainability)**")
            if explanation:
                exp_df = pd.DataFrame(
                    sorted(explanation.items(), key=lambda x: abs(x[1]), reverse=True)[:8],
                    columns=["Feature", "Impact"]
                ).set_index("Feature")
                st.bar_chart(exp_df, height=260)
                st.caption("Positive bars push risk up, negative bars push risk down — based on model feature importance and your answers.")
            else:
                st.info("Explainability data not available.")
            glass_card_end()

            st.success("Saved to your dashboard health trend ✅")

        except Exception as e:
            st.error(f"API error: {e}")