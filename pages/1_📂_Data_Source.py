import streamlit as st
from datasets import original_dataset, cleaned_dataset, dataset_used

# Dataset overview
st.markdown("# Dataset used for the program")
st.sidebar.markdown("# Dataset source: ")
st.sidebar.write("**Platform:** Kaggle")
st.sidebar.write("**Titles:**")
st.sidebar.write("1. Behavioural Tweets")
st.sidebar.write("2. Depression: Twitter Dataset + Feature Extraction")
st.sidebar.write("3. Sentimental Analysis for Tweets")
st.sidebar.write("4. Preprocessed Depression Dataset")
st.sidebar.write("**Authors:**")
st.sidebar.write("1. ARSH KANDROO")
st.sidebar.write("2. INFAMOUSCODER")
st.sidebar.write("3. SHINIGAMI")
st.sidebar.write("4. MD. FORIDUZZAMAN ZIHAD, MD. REZUWAN HASSAN")
st.sidebar.write("**Source:** Twitter")
st.sidebar.write("**Url:** ")
st.sidebar.write("1. https://www.kaggle.com/datasets/arshkandroo/behavioural-tweets")
st.sidebar.write("2. https://www.kaggle.com/datasets/infamouscoder/mental-health-social-media")
st.sidebar.write("3. https://www.kaggle.com/datasets/gargmanas/sentimental-analysis-for-tweets")
st.sidebar.write("4. https://www.kaggle.com/datasets/mdforiduzzamanzihad/preprocessed-depression-dataset")
st.sidebar.write("**About:** These datasets contain social media texts scraped from Twitter, and later merged into 1 dataset")
st.sidebar.write(" ")
st.sidebar.write("**Features:**")
st.sidebar.write("text - Social media text")
st.sidebar.write("mental_health_label - Label category for each text (Depression/Anxiety/Neutral)")


st.write("Original dataset: ", original_dataset)
st.write("Dataset after cleaning and formatting: ", cleaned_dataset)
st.write("Dataset used: ", dataset_used)
