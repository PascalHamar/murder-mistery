# storygenerator.py

import openai

client = openai.OpenAI()

def generate_story_from_prompt(file_path):
    # Lesen des Prompts aus der Datei mit UTF-8-Kodierung
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Senden des Prompts an GPT-4 und Empfangen der Antwort
    response = client.chat.completions.create(
        model="gpt-4",  # Sie können das gewünschte Modell hier spezifizieren
        messages=[{"role": "system", "content": "Dies ist ein Story-Generator."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content