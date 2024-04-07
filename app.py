import base64
from dotenv import load_dotenv
import streamlit as st
import os 
import io
from PIL import Image
import pdf2image
import google.generativeai as gai


load_dotenv()

gai.configure(api_key=os.getenv('GEN_API_KEY'))

def get_gemini_response(input, pdf_content,prompt):
    model = gai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0],prompt])
    return response.text

def get_pdf_parts(upload_file):
    if upload_file:
        images = pdf2image.convert_from_bytes(upload_file.read())
        first_page = images[0] 

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                'mime_type': 'image/jpeg',
                'data': base64.b64encode(img_byte_arr).decode()
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError('File not found')

def button1_sumbit():
    prompt = """
        You are an experienced HR with tech experience in the field of the full stack web development, aws cloud expert, .netcore, devops, your task is to review the provided 
        resume against the job description for these profiles.
        Please share your professional evaluation on whether the candidate's profile aligns with the role.
        Highlight the strengths and weaknesses of the applicant in relation to the specified job.
        """
    if uploaded_file is not None:
        pdf_content = get_pdf_parts(uploaded_file)
        response = get_gemini_response(input, pdf_content, prompt)
        st.subheader("The response is ")
        with right_column:
            st.write(response)
    else:
        st.write("Please upload your resume")

def button2_sumbit():
    prompt = """
    You are an skilled ATS (Application Tracking System) scanner with a deep understanding of full stack web development, aws cloud expert, .netcore, devops, and deep ATS functionality
    Your task is to evaluate the resume against the job description. give me the percentage of match if the resume matches 
    the job description. First the output should come as percentage and then keywords missing and last final thoughts.
    """
    if uploaded_file is not None:
        pdf_content = get_pdf_parts(uploaded_file)
        response = get_gemini_response(input, pdf_content, prompt)
        st.subheader("The response is ")
        with right_column:
            st.write(response)
    else:
        st.write("Please upload your resume")


# Streamlit App
st.set_page_config(page_title="ATS resume expert", page_icon=":gem:",layout="wide")
st.header("ATS resume expert")
left_column, right_column = st.columns(2)

with left_column:
    input = st.text_area("Job description: ", key="input")
    uploaded_file = st.file_uploader("Upload your resume", type="pdf")

    if uploaded_file is not None:
        st.write("PDF file uploaded")


    buttons =   [
                st.button("Tell me about my resume", key="button1", on_click=button1_sumbit), 
                st.button("Percentage match", key="button2", on_click=button2_sumbit)
                ]

with right_column:
    st.info("This is your response for profile and job description match -\n")