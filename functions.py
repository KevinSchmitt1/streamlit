import streamlit as st

def navigation():
    '''
    Function to customize the navigation sidebar panel
    '''
    st.sidebar.page_link('app.py', label="👋🏻 Welcome")
    st.sidebar.page_link('pages/01_eda.py', label="📊 EDA")
    st.sidebar.page_link('pages/02_predictions.py', label="🧠 Prediction")
    st.sidebar.page_link('pages/03_map.py', label="🌍 Map")