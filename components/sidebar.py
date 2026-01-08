import streamlit as st
from streamlit_option_menu import option_menu

def sidebar(menu_items):
    with st.sidebar:
        st.markdown("## 🏥 MediCare")
        selected = option_menu(
            "",
            menu_items,
            icons=["activity", "flask", "capsule", "building", "credit-card", "people", "shield", "truck", "bar-chart"],
            default_index=0
        )

        st.divider()
        if st.button("Logout"):
            st.session_state.page = "login"
            st.session_state.role = None
            st.rerun()

    return selected
