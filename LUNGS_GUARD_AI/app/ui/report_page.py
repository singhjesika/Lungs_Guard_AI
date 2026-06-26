import streamlit as st
from pathlib import Path
from app.ui.theme import glass_card_start, glass_card_end


def render():
    st.markdown('<div class="glow-title">📄 Patient Reports</div>', unsafe_allow_html=True)
    glass_card_start()
    report_dir = Path("reports/pdf_reports")
    reports = list(report_dir.glob("*.pdf")) if report_dir.exists() else []
    if not reports:
        st.info("No PDF reports generated yet. Reports will appear here once exported.")
    else:
        for r in reports:
            with open(r, "rb") as f:
                st.download_button(label=r.name, data=f, file_name=r.name, mime="application/pdf")
    glass_card_end()