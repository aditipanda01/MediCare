import streamlit as st
from components.sidebar import sidebar
from views.category_modules import category_modules
from components.charts import patient_line_chart, appointment_donut_chart


def patient_dashboard():
    # ---------- Session Defaults ----------
    st.session_state.setdefault("view", "dashboard")
    st.session_state.setdefault("selected_category", None)

    # ---------- Sidebar ----------
    sidebar([
        "A - Clinical Data",
        "B - Laboratory",
        "C - Pharmacy",
        "D - Hospital Ops",
        "E - Billing",
        "F - HR & Staff",
        "G - Compliance",
        "H - Supply Chain",
        "I - Analytics"
    ])

    # ---------- Module View ----------
    if st.session_state.view == "modules":
        category_modules()
        return

    # ---------- Dashboard View ----------
    st.markdown("## Welcome back, Sarah 👋")
    st.markdown("Here’s an overview of your health dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.button("📅 Book Appointment")
    c2.button("📄 View Reports")
    c3.button("💊 My Prescriptions")
    c4.button("🧪 Lab Results")

    st.divider()

    st.subheader("Your Health Categories")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🩺 A - Clinical Data", use_container_width=True):
            st.session_state.selected_category = "A - Clinical Data"
            st.session_state.view = "modules"
            st.rerun()

    with col2:
        if st.button("🧪 B - Laboratory", use_container_width=True):
            st.session_state.selected_category = "B - Laboratory"
            st.session_state.view = "modules"
            st.rerun()

    # ---------- Charts (ONLY INSIDE DASHBOARD) ----------
    st.divider()
    st.subheader("Health Insights")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        patient_line_chart()

    with chart_col2:
        appointment_donut_chart()
