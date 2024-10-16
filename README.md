# Question Bank Generator

The **Question Bank Generator** is a tool that automatically generates a question bank based on course notes, using **LangChain**, **Gemini API**, and **Streamlit**.

## Features

- Upload course materials (PDF, DOCX, or TXT).
- Generates questions based on Bloom’s Taxonomy.
- Uses **Gemini API** for text processing.
- Built with **Streamlit** for an easy-to-use interface.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Rakshithg6/Question_Bank_Generator.git
    cd Question_Bank_Generator
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1. **Set up the API key** in a `.env` file:

    ```bash
    GEMINI_API_KEY=your_api_key_here
    ```

2. **Run the app:**

    ```bash
    streamlit run app.py
    ```

Open your browser and go to `http://localhost:8501` to use the application.

## License

This project is licensed under the MIT License.
