import streamlit as st
from transformers import pipeline
from summarizer import Summarizer
import os
from huggingface_hub import login

huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
login(huggingface_token)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", use_auth_token=True)

input_text='In evaluating the quality of machine-generated summaries, ROUGE & BERTScore are commonly used metrics, each with unique benefits. ROUGE (Recall-Oriented Understudy for Gisting Evaluation) emphasizes the syntactic overlap between the generated and reference summaries. It does so by measuring the recall of unigrams (ROUGE-1), bigrams (ROUGE-2), and the longest common subsequence (ROUGE-L). This helps determine how much key information from the reference summary is present in the generated summary. Higher ROUGE scores mean greater similarity between summaries, indicating higher quality.'

# Title of the application
st.title("Hugging Face Text Summarization")

# Description
st.write("This application summarizes the input text using DistilBERT.")

inputs = tokenizer(input_text, return_tensors="pt")

# Generate text using the model
output = model.generate(inputs['input_ids'], max_length=100)

# Decode the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

st.write(generated_text)

# Text input from the user
# user_input = st.text_area("Enter the text you want to summarize", height=250)

# summary_bert_transformer = model(main_content, num_sentences=7)

# # Load the summarization pipeline
# def load_model():
#     # summarizer = pipeline("summarization", model="distilbert-base-uncased")
#     summarizer = Summarizer('distilbert-base-uncased', hidden=[-1,-2], hidden_concat=True)

#     return summarizer

# summarizer = load_model()

# # Button to generate the summary
# if st.button("Summarize"):
#     if user_input:
#         # Perform summarization
#         summary = summarizer(user_input, num_sentences=7)
#         # Display the summary
#         st.subheader("Summary")
#         st.write(summary)
#     else:
#         st.write("Please enter some text to summarize.")

# Footer
st.write("Developed using Streamlit and Hugging Face Transformers")
