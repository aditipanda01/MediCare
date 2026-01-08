# app.py
import streamlit as st
from auth.login import login_page
from auth.signup import signup_page
from dashboards.patient_dashboard import patient_dashboard
from dashboards.doctor_dashboard import doctor_dashboard

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="MediCare", layout="wide")

# ---------------- SESSION STATE INIT ----------------
# Initialize session state variables if they don't exist
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("page", "login")
st.session_state.setdefault("role", None)
st.session_state.setdefault("view", "dashboard")
st.session_state.setdefault("selected_category", None)
st.session_state.setdefault("selected_module", None)

# ---------------- ROUTING ----------------
# If not logged in, show login/signup pages
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()

# If logged in, show dashboard based on role
else:
    if st.session_state.role == "Patient":
        patient_dashboard()
    elif st.session_state.role == "Doctor":
        doctor_dashboard()
    elif st.session_state.role == "Admin":
        st.title("🛠 Admin Dashboard (Coming Soon)")

# ---------------- OPTIONAL: Quick Routing Fix ----------------
# If somehow logged_in is True but page is still "login" or "signup", redirect to dashboard
if st.session_state.logged_in and st.session_state.page in ["login", "signup"]:
    st.session_state.page = "dashboard"
    st.rerun()
