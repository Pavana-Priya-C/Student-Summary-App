import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

@st.cache_resource
def load_summarization_model():
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_summarization_model()

st.title("Text Summarization with BART")

input_text = st.text_area("Enter the text you want to summarize", height=200)

if st.button("Summarize"):
    if input_text.strip():
        inputs = tokenizer([input_text], max_length=1024, return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.error("Please enter some text to summarize.")
