from appinterface2 import second_page
from appinterface3 import main_page
import streamlit as st
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
#hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
#login(hf_token)

# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'main_page'

# Render the appropriate page based on session state
if st.session_state.page == 'main_page':
    main_page()
elif st.session_state.page == 'second_page':
    second_page()

