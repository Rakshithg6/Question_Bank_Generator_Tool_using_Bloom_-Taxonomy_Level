import streamlit as st
import fitz  # PyMuPDF for PDF processing
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Set your Google API key directly here
google_api_key = "AIzaSyDUgOcQy1AokHighaXjxFlEYqpu6cSmP9I"  # Replace with your actual Google API key
genai.configure(api_key=google_api_key)

# Set up the Streamlit page configuration (optional)
st.set_page_config(page_title="Question Bank Generator Tool", layout="centered")

# Title of the app
st.title("Question Bank Generator Tool using Bloom's Taxonomy")

# PDF upload widget
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    st.write("### Extracted Text:")  # Debug: Show extracted text
    st.write(text[:10000000] + "...")  # For brevity, only display first 10000000 characters
    return text

def get_question_generation_chain():
    # Updated prompt with Bloom's Taxonomy
    # Updated prompt with Bloom's Taxonomy
    prompt_template = """
You are tasked with generating a question bank using Bloom's Taxonomy from the provided content.

Your task is to generate 4 questions for each level of Bloom's taxonomy based on the following verbs:
1. Knowledge-based questions should use verbs such as define, memorize, repeat, copy, identify, state, list, quote, or find. Avoid using question starters like 'what', 'how', 'why', 'when', or 'where'.
2. Comprehension-based questions should use verbs like summarize, compare, describe, explain, discuss, recognize, report, translate, and categorize. Avoid question starters like 'what', 'how', 'why', 'when', or 'where'.
3. Application-based questions should use verbs like determine, present, examine, implement, solve, use, demonstrate, interpret, and reenact. Avoid question starters like 'what', 'how', 'why', 'when', or 'where'.
4. Analysis-based questions should use verbs such as organize, compare, contrast, experiment, test, question, connect, deduce, and link. Avoid using question starters like 'what', 'how', 'why', 'when', or 'where'.
5. Synthesis-based questions should use verbs like design, compose, construct, develop, formulate, blog, build, write, or simulate. Avoid question starters like 'what', 'how', 'why', 'when', or 'where'.
6. Evaluation-based questions should use verbs such as argue, defend, judge, support, value, weigh, reflect, review, and grade. Avoid using question starters like 'what', 'how', 'why', 'when', or 'where'.

Context:
{context}

Generate at least 4 questions for each level of Bloom's Taxonomy based on the provided content, and ensure each question ends with a . Avoid using colons in the questions and do not bold the keyword.
"""



    # Define the model for Google Generative AI
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Updated model name, based on available Gemini API models
        client=genai,
        temperature=0.6,
        google_api_key=google_api_key
    )

    # Initialize the PromptTemplate
    prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

    # Create an LLM chain using the prompt and model
    chain = LLMChain(llm=model, prompt=prompt)
    return chain

# Generate questions in the main processing function
# Generate questions in the main processing function
def process_pdf_for_questions(extracted_text):
    st.write("### Processing PDF for Questions...")  # Debug statement
    if not extracted_text:
        st.error("No text extracted from PDF.")
        return None

    chain = get_question_generation_chain()

    # Prepare the context for the prompt
    response = chain.run(context=extracted_text)  # Pass the extracted_text as context
    st.write("### Response from Chain:")  # Debug statement
    st.write(response)  # Debug: Show raw response


# If a PDF is uploaded
if uploaded_file is not None:
    # Display the uploaded PDF (optional: Show file name or pages)
    st.write("### Uploaded PDF:")
    st.write(uploaded_file.name)

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(uploaded_file)

    # Generate Questions Button
    if st.button("Generate Questions"):
        with st.spinner("Generating questions..."):
            # Generate questions from the extracted text using Bloom's Taxonomy
            generated_questions = process_pdf_for_questions(extracted_text)

            # Display generated questions
            if generated_questions:
                st.write("### Generated Questions:")
                for idx, question in enumerate(generated_questions, start=1):
                    st.write(f"{idx}. {question['output']}")
            
