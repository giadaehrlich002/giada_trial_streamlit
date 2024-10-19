import streamlit as st
import pandas as pd


st.title('Visualisation Results of Cracks dataset❤️')
st.info("this app shows the training results of the object detection on the cract dataset")
st.write('Welcome')
st.write('modification')

with st.expander('Data'): 
  st.write('**Raw data**')
  # you have to type in the path of the raw data"
  df = pd.read_csv('https://raw.githubusercontent.com/giadaehrlich002/giada_trial_streamlit/refs/heads/master/happiness2020.csv')
  df
  
