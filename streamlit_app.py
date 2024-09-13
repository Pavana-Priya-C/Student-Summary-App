import streamlit as st
import re
from streamlit_option_menu import option_menu
import os
from PIL import Image
from preprocessing import extract_text_from_pdf, preprocess_text_chap8, preprocess_text, get_title, remove_subsequent_occurrences, separate_sections, get_title6_9, get_title_5
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the BART model and tokenizer
@st.cache_resource
def load_bart_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_bart_model()

# Function to split text into smaller chunks
def chunk_text(text, chunk_size=512):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])


# Set the title of the web app
st.title("Welcome to Future Minds Tutoring")

# Sidebar with navigation options
with st.sidebar:
    option = option_menu("Menu",
                        options=["About Us","Chapter Summary"],
                        icons=['house-fill','search'])

if option == "About Us":
    # Load and resize the image
    img = Image.open("images/Future min.jpg")
    
    # Specify the desired height
    desired_height = 250
    # Calculate the width to maintain the aspect ratio
    width, height = img.size
    aspect_ratio = width / height
    new_width = int(desired_height * aspect_ratio)
    
    # Resize the image
    img = img.resize((new_width, desired_height))
    
    # Display the resized image
    st.image(img, use_column_width=True)

    st.header("About Us")
    st.write("""
    At Future Minds Tutoring, we deliver outstanding educational support to students in grades 10, 11, and 12. Our innovative methodology blends conventional pedagogy with state-of-the-art artificial intelligence technologies to provide all-encompassing and customized learning experiences.

    Our professional educators and AI specialists collaborate to generate chapter-specific content that is simplified and easy to understand, allowing students to grasp and retain information more quickly. Our dedication lies in providing specialized resources and support to kids with exceptional needs, enabling them to overcome obstacles and excel academically.
    """)

    st.header("Mission")
    st.write("""
    Our mission is to provide high-quality, inclusive education to students of classes 10, 11, and 12, fostering an environment where every student, including those with special needs, can excel. We leverage advanced AI technology to deliver personalized and effective learning experiences that help students understand and retain complex concepts.
    """)
    
    st.header("Vision")
    st.write("""
    Our vision is to be a leading educational institution recognized for our commitment to academic excellence and inclusivity. We aim to transform traditional learning by integrating innovative AI solutions, ensuring that every student, regardless of their challenges, has the opportunity to succeed and achieve their full potential.
    """)
    
    

elif option == "Chapter Summary":
    st.subheader("Chapter Summary")
    # File upload section
        
    uploaded_file = st.file_uploader("Upload your file :", type=["pdf"])

    if uploaded_file is not None:
        filename = uploaded_file.name

        if uploaded_file.type == "application/pdf":

            # st.write(f"File Name: {filename}")
            st.success("File uploaded successfully! Please wait for the summary...")
            if filename == 'jefp108.pdf':
                # Extract text from the uploaded PDF file
                raw_text = extract_text_from_pdf(uploaded_file)
                title = get_title(raw_text)
                preprocessed_text = preprocess_text_chap8(raw_text)
                preprocessed_text = preprocess_text(preprocessed_text)
                
                 # Remove subsequent occurrences of the title
                clean_text = remove_subsequent_occurrences(preprocessed_text, title)

                # Separate sections of the text
                main_content, glossary, think_about_it, talk_about_it, suggested_reading = separate_sections(clean_text)
                    
                # Split the text into smaller chunks and summarize each chunk
                summarized_text = ""
                for chunk in chunk_text(main_content):
                    inputs = tokenizer(chunk, max_length=1024, return_tensors="pt", truncation=True)
                    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=200, length_penalty=2.0)
                    summarized_chunk = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                    summarized_text += summarized_chunk + " "

                st.subheader(f'Summary of {title}: \n {summarized_text}')   
            else:
                
                raw_text = extract_text_from_pdf(uploaded_file)

                if filename == 'jefp106.pdf' or filename == 'jefp109.pdf':
                    title = get_title6_9(raw_text)
                    # st.write(title)
                
                elif filename == 'jefp105.pdf':
                    title = get_title_5(raw_text)
                    # st.write(title)

                else:
                    title = get_title(raw_text)    
                    # st.write(title)

                cleaned_text = preprocess_text(raw_text)
                cleaned_text = remove_subsequent_occurrences(cleaned_text, title)


                # Separate sections of the text
                main_content, glossary, think_about_it, talk_about_it, suggested_reading = separate_sections(cleaned_text)
                # Split the text into smaller chunks and summarize each chunk
                summarized_text = ""
                for chunk in chunk_text(main_content):
                    inputs = tokenizer(chunk, max_length=1024, return_tensors="pt", truncation=True)
                    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=200, length_penalty=2.0)
                    summarized_chunk = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
                    summarized_text += summarized_chunk + " "

                st.subheader(f'Summary of {title}: \n {summarized_text}')     

        else:
            st.error("Please upload a valid PDF file.")
            

    else:
        st.warning("Please upload a file.")     






# Footer
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("***")
st.write("© 2024 Future Minds Tutoring. All rights reserved.")  





