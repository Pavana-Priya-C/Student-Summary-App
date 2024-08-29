import streamlit as st
from transformers import pipeline

# Title of the application
st.title("DistilBERT Text Summarization")

# Description
st.write("This application summarizes the input text using DistilBERT.")

# Text input from the user
user_input = st.text_area("Enter the text you want to summarize", height=250)

# Load the summarization pipeline
@st.cache_resource
def load_model():
    summarizer = pipeline("summarization", model="distilbert-base-uncased")
    return summarizer

summarizer = load_model()

# Button to generate the summary
if st.button("Summarize"):
    if user_input:
        # Perform summarization
        summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
        # Display the summary
        st.subheader("Summary")
        st.write(summary[0]['summary_text'])
    else:
        st.write("Please enter some text to summarize.")

# Footer
st.write("Developed using Streamlit and Hugging Face Transformers")
