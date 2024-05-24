import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Bitcoin")

output5 = Image.open('output5.png')
st.image(output5)

if st.button('Predict'):
  output1 = Image.open('output1.png')
  st.image(output1)

if st.button('Predict Next 30Days'):
      output3 = Image.open('output3.png')
      st.image(output3)

Bitcoin = pd.read_csv('Bitcoin.csv')
Bitcoin1 = dataframe_explorer(Bitcoin,case=False)
st.dataframe(Bitcoin1, use_container_width=True)
