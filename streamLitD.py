import streamlit as st
import pandas as pd

data = pd.read_csv("D:\AIML-Dataset.csv")

st.write("""#My First App
        Hello World
        """)

st.table(data)