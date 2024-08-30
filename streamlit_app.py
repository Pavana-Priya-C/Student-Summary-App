import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image


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
    chapter_num = st.selectbox("Choose the chapter for reading",
                                           options=['Chapter 1 - A Triumph of Surgery',
                                                    'Chapter 2 - The Theif\'s Story',
                                                    'Chapter 3 - The midnight visitor',
                                                    'Chapter 4 - A Question of Trust',
                                                    'Chapter 5 - Footprints with Feet',
                                                    'Chapter 6 - The Making of a Scientist',
                                                    'Chapter 7 - The Necklace',
                                                    'Chapter 8 - Bholi',
                                                    'Chpater 9 - The Book That Saved the Earth'])
    
    if chapter_num == 'Chapter 1 - A Triumph of Surgery':
        tab1,tab2 = st.tabs(['Summary 1', 'Summary 2'])
        with tab1:
            file_path = "data/chap1-t5base.txt"
            with open(file_path, "r") as file:
                file_content = file.read()

            # Display the file content
            st.write(file_content)

    else:
        st.write('Select the chapter...')      








# Footer
st.markdown("***")
st.write("© 2024 Future Minds Tutoring. All rights reserved.")  
