import streamlit as st 
import pandas as pd


df = pd.read_csv('spotify.csv')
df[df["Stream"] >  1000000]
df

print(df.columns)

