# auth/login.py
import streamlit as st

def login_page():
    st.title("🏥 MediCare Login")

    # --- Login Form ---
    role = st.selectbox("Login as", ["Patient", "Doctor", "Admin"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # For demo purposes, assume login always succeeds
        st.session_state.logged_in = True
        st.session_state.role = role
        st.session_state.page = "dashboard"  # <-- switch page
        st.rerun()

    # --- Signup link ---
    st.markdown("Don't have an account?")
    if st.button("Signup"):
        st.session_state.page = "signup"
        st.rerun()
