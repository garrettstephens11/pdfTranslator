# pdfTranslator
user is prompted to upload a pdf, the text is extracted from it in english, then the user clicks 'translate' and the text shows up as translated into spanish on the next page

**Credit: I created this by asking ChatGPT-4 to walk me through how to make this application to these specifications, and even had ChatGPT generate this readmefile

# PDF Translator

This application allows you to translate text extracted from PDF files. It's designed to be fast and efficient, using `C` and `poppler` for text extraction and the Google Cloud Translate API for translation.

## Key Features
- Fast and efficient PDF text extraction using `C` and `poppler`.
- Translation powered by Google Cloud Translate API.
- Simple and easy to use.

## Prerequisites
- Python 3.8 or higher
- Flask
- A Google Cloud account

**Note:** To use the Google Cloud Translate API, you will need your own Google Cloud account and an API key. This is not provided as part of this project.

## Getting Started

### Setting Up Your Google Cloud Account

1. Create a Google Cloud account if you don't have one already: [Google Cloud](https://cloud.google.com/).
2. Follow the instructions to create a new project.
3. Enable the Cloud Translation API for your project. You can find this in the "APIs & Services" dashboard.
4. Create an API key. Save this in a secure place.

### Setting Up the Project

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/pdf_translator.git
    ```

2. Change into the project directory.

    ```bash
    cd pdf_translator
    ```

3. Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

4. Create an environment variable for your Google Cloud API key.

    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/api/key.json"
    ```

5. Run the Flask server.

    ```bash
    export FLASK_APP=app.py
    flask run
    ```

Visit `http://127.0.0.1:5000` in your web browser to use the application.
