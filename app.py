import streamlit as st
import pandas as pd
from functions import navigation

st.set_page_config(page_title='Pokemon - Streamlit Demo', page_icon=':smile:', layout='wide')

navigation()

#Write title/headers/text
st.title('Welcome to my Pokemon - Streamlit Demo!')
st.subheader('Let\'s explore the world of Pokemon together!')
st.image('images/pokemon.png')


st.subheader('What are we going to do?')
st.write("")
st.markdown('- EDA Visualizations / Dataset exploration \n - __Prediction:__ Is my Pokémon legendary? \n - Find our Pokémon in the map')



# Save variables in the session state
st.session_state.df = pd.read_csv('data/pokemon.csv')
st.session_state.stats_cols = ['hit_points', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']