import streamlit as st
from PIL import Image

st.markdown("# Exploratory Data Analysis")
st.write(" ")
st.write("**1. Distribution of Mental Health Label**")
st.image(Image.open("dist of mental health labels.png"), use_column_width=True)
st.image(Image.open("dist of mental health labels (pie).png"), use_column_width=True)
st.write(" ")
st.write("**2. Distribution of Text Length**")
st.image(Image.open("dist of text length.png"), use_column_width=True)
st.write(" ")
st.write("**3. Average Text Length by Mental Health Label**")
st.image(Image.open("avg text length for each label.png"), use_column_width=True)
st.write(" ")
st.write("**4. Word Cloud**")
st.write("Word Cloud for Overall Dataset")
st.image(Image.open("WC overall.png"), use_column_width=True)
st.write(" ")
st.write("Word Cloud for 'Stress' Label")
st.image(Image.open("WC stress.png"), use_column_width=True)
st.write(" ")
st.write("Word Cloud for 'Anxiety' Label")
st.image(Image.open("WC anxiety.png"), use_column_width=True)
st.write(" ")
st.write("Word Cloud for 'Depression' Label")
st.image(Image.open("WC depression.png"), use_column_width=True)


