import streamlit as st
from transformers import pipeline
from summarizer import Summarizer


# Title of the application
st.title("DistilBERT Text Summarization")

# Description
st.write("This application summarizes the input text using DistilBERT.")

# Text input from the user
user_input = st.text_area("Enter the text you want to summarize", height=250)

# summary_bert_transformer = model(main_content, num_sentences=7)

# Load the summarization pipeline
def load_model():
    # summarizer = pipeline("summarization", model="distilbert-base-uncased")
    summarizer = Summarizer('distilbert-base-uncased', hidden=[-1,-2], hidden_concat=True)

    return summarizer

summarizer = load_model()

# Button to generate the summary
if st.button("Summarize"):
    if user_input:
        # Perform summarization
        summary = summarizer(user_input, num_sentences=7)
        # Display the summary
        st.subheader("Summary")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

# Footer
st.write("Developed using Streamlit and Hugging Face Transformers")
