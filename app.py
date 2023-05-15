import os
import subprocess
from flask import Flask, render_template, request, send_file
from google.cloud import translate_v2 as translate

app = Flask(__name__)

translate_client = translate.Client()

def extract_text_from_pdf(pdf_path):
    process = subprocess.Popen(['./pdf_reader', pdf_path], stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode('utf-8')

def translate_text(text):
    max_chunk_size = 5000  # You can adjust this value
    translations = []

    for i in range(0, len(text), max_chunk_size):
        chunk = text[i:i+max_chunk_size]
        result = translate_client.translate(chunk, target_language='es')
        translations.append(result['translatedText'])

    translated_text = ' '.join(translations)
    return translated_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        return render_template('index.html', text=text)

    return render_template('index.html', text=None)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    translated_text = translate_text(text)
    return render_template('translate.html', text=translated_text)
