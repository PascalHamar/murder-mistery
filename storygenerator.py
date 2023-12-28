# storygenerator.py
import openai
import os

openai.api_key = os.getenv['OPENAI_API_KEY']

def generate_story_from_prompt(file_path):
    # Lesen des Prompts aus der Datei mit UTF-8-Kodierung
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Senden des Prompts an GPT-4 und Empfangen der Antwort
    response = openai.Completion.create(
        model="gpt-4",  # Sie können das gewünschte Modell hier spezifizieren
        prompt=prompt,
        max_tokens=150
    )

    return response.choices[0].text.strip()
