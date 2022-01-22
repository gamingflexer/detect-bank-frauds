import numpy as np
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import missingno as msno

st.title("Hello world!")

st.write("""#My First App
        Hello World
        """)

data = pd.read_csv("Dtest-30.csv")

def list_chunks(initial_list: list, size: int = 20):
    for x in range(0, len(initial_list), size):
        yield initial_list[x:x + size]


for columns in list_chunks(data.columns):
    msno.bar(data[columns])
    plt.show()

fig, ax = plt.subplots()
data.hist(
    bins=8,
    column="amount",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=9,
    rwidth=0.2,
    ax=ax,
)
st.write(fig)