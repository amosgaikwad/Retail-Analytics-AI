import streamlit as st

def load_theme():
    st.markdown("""
    <style>
    .stApp{
        background:#0B1120;
    }
    </style>
    """, unsafe_allow_html=True)