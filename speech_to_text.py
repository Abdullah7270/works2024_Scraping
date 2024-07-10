from groq import Groq 
import os 
from dotenv import load_dotenv
from docx import Document

load_dotenv()
api_key= os.environ['GROQ_API_KEY']

client = Groq(api_key=api_key)

def audio_to_text(filepath):
    with open(filepath, 'rb') as file:
        translation = client.audio.translations.create(
            file = (filepath, file.read()),
            model= 'whisper-large-v3',
        )
        return translation.text
translation_text = audio_to_text('speech.mp3')
print(translation_text)

doc = Document()
doc.add_paragraph(translation_text)
doc.save('Job Interview Essentials.docx')
print('Audio file transcribed and saved successfully.')