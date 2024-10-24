# Question Bank Generator Tool

The **Question Bank Generator** is a tool designed to automatically generate a comprehensive question bank based on provided course materials. This tool utilizes **LangChain**, **Gemini API**, and **Streamlit** to offer an intuitive interface for users.

## Features

- **File Upload**: Users can upload course materials in various formats, including PDF, DOCX, and PPT.
- **Question Generation**: Automatically generates questions based on **Bloom's Taxonomy**, tailored to the content of the uploaded materials.
- **Text Processing**: Utilizes **Gemini API** for efficient text processing and extraction from uploaded files.
- **User-Friendly Interface**: Built with **Streamlit**, providing a seamless user experience.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rakshithg6/Question_Bank_Generator_Tool_using_Bloom_-Taxonomy_Level.git
    cd Question_Bank_Generator_Tool_using_Bloom_-Taxonomy_Level
    ```

2. **Install dependencies**:

    Ensure you have Python installed. Then, install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1. **Set up the API key**:
   Create a `.env` file in the root of the project directory and add your Gemini API key:

    ```plaintext
    GEMINI_API_KEY=your_api_key_here
    ```

2. **Run the application**:

    ```bash
    streamlit run app.py
    ```

3. **Access the app**: 
   Open your web browser and go to `http://localhost:8501` to use the Question Bank Generator.

## Usage

- Upload your course material using the upload button.
- Select the subject from the dropdown menu.
- Click on the "Generate Questions" button to see the generated questions based on the uploaded material.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **LangChain**: For facilitating the creation of question banks.
- **Gemini API**: For efficient text processing.
- **Streamlit**: For building the web application interface.
