import streamlit as st
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

st.title("Neocoin")

outputN2 = Image.open('outputN2.png')
st.image(outputN2)

if st.button('Predict'):
      outputN = Image.open('outputN.png')
      st.image(outputN)

if st.button('Predict Next 30Days'):
     outputN1 = Image.open('outputN1.png')
     st.image(outputN1)
    
Neocoin = pd.read_csv('NEOCoin.csv')
Neocoin1 = dataframe_explorer(Neocoin,case=False)
st.dataframe(Neocoin1, use_container_width=True)
