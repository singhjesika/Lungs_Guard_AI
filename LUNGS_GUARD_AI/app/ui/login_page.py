import streamlit as st
from app.ui.theme import inject_css, animated_lung


def render():
    inject_css()
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.4, 1])
    with col2:
        animated_lung()
        st.markdown('<div class="glow-title" style="text-align:center;">LungsGuard AI</div>', unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align:center; color:#9CA3AF;'>Your AI companion for early lung cancer risk detection</p>",
            unsafe_allow_html=True,
        )

        with st.container():
            name = st.text_input("Patient Name", placeholder="Enter your name")
            age = st.number_input("Age", min_value=1, max_value=120, value=30)
            if st.button("Enter Dashboard →", use_container_width=True):
                if name.strip():
                    st.session_state["patient_name"] = name.strip()
                    st.session_state["patient_age"] = age
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.warning("Please enter your name to continue.")

        st.markdown(
            "<p style='text-align:center; color:#6B7280; font-size:0.8rem; margin-top:1.5rem;'>"
            "🔒 No data leaves your device beyond this session.</p>",
            unsafe_allow_html=True,
        )