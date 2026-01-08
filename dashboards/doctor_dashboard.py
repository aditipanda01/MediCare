import streamlit as st
from components.sidebar import sidebar
from views.category_modules import category_modules
from components.charts import patient_line_chart, appointment_donut_chart


def doctor_dashboard():
    # ---------- Session Defaults ----------
    st.session_state.setdefault("view", "dashboard")
    st.session_state.setdefault("selected_category", None)

    # ---------- Sidebar ----------
    category = sidebar([
        "Patients",
        "Appointments",
        "Reports",
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

    # ---------- Route to Modules ----------
    if category and category.startswith(("A -", "B -", "C -", "D -", "E -", "F -", "G -", "H -", "I -")):
        st.session_state.selected_category = category
        st.session_state.view = "modules"
        category_modules()
        return

    # ---------- Master Dashboard ----------
    st.markdown("## 🩺 Master Dashboard")
    st.markdown("Welcome back! Here's your hospital overview.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Patients", "12,450", "+12%")
    c2.metric("Active Alerts", "320", "-5%")
    c3.metric("Lab Reports", "185", "+8%")
    c4.metric("Prescriptions", "750", "+15%")

    st.divider()

    st.subheader("Your Patients Today")
    st.success("10:30 AM – Sarah Hostern (Bronchitis)")
    st.info("11:00 AM – Dakota Smith (Stroke)")
    st.warning("11:30 AM – John Lane (Liver)")

    # ---------- Charts (ONLY HERE) ----------
    st.divider()
    st.subheader("Hospital Insights")

    col1, col2 = st.columns(2)

    with col1:
        patient_line_chart()

    with col2:
        appointment_donut_chart()
