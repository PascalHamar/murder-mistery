import streamlit as st
from openai import OpenAI
import os

try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
    api_key = None

if not api_key:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY nicht in Umgebungsvariablen gefunden. Stellen Sie sicher, dass er gesetzt ist.")

client = OpenAI(api_key=api_key)

def generate_story_from_prompt(file_path):
    # Lesen des Prompts aus der Datei mit UTF-8-Kodierung
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Senden des Prompts an GPT-4 und Empfangen der Antwort
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message.content
