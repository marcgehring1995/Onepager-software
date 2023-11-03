
import streamlit as st
import login
import main_app

st.set_page_config(layout='wide')
# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Create login form
if not st.session_state['logged_in']:
    login.app()
else:
    main_app.app()