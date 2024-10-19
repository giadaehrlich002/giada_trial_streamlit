import streamlit as st
import pandas as pd


st.title('Visualisation Results of Cracks dataset❤️')
st.info("this app shows the training results of the object detection on the cract dataset")
st.write('Welcome')

with st.expander('Data'): 
  st.write('**Raw data**')
  df = pd.read_csv('https://github.com/giadaehrlich002/giada_trial_streamlit/blob/master/happiness2020.csv')
  
