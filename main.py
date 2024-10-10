import streamlit as st
import fitz  # PyMuPDF for PDF processing

# Set up the Streamlit page configuration (optional)
st.set_page_config(page_title="Question Bank Generator Tool", layout="centered")

# Title of the app
st.title("Question Bank Generator Tool")

# PDF upload widget
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# Function to generate questions from text (placeholder logic, replace with your own logic)
def generate_questions_from_text(text):
    # For demonstration purposes, we'll just return a few mock questions
    questions = [
        "What is the main topic discussed in the document?",
        "List the key points mentioned in the document.",
        "Summarize the conclusions of the document."
    ]
    return questions

# If a PDF is uploaded
if uploaded_file is not None:
    # Display the uploaded PDF (optional: Show file name or pages)
    st.write("### Uploaded PDF:")
    st.write(uploaded_file.name)

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(uploaded_file)

    # Generate Questions Button
    if st.button("Generate Questions"):
        # Generate questions from the extracted text
        generated_questions = generate_questions_from_text(extracted_text)

        # Display the generated questions
        st.write("### Generated Questions:")
        for idx, question in enumerate(generated_questions, start=1):
            st.write(f"{idx}. {question}")
