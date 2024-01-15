import streamlit as st
import openai

'''client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])'''
client = openai.Completion(api_key="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")

def generate_from_prompt(file_path, story, anzahl_charaktere):
    
    if story and anzahl_charaktere:
        # Mit Story UND anzahl_charaktere als Argumente werden Charaktere generiert, sonst wird die Story generiert
        
        
        prompt = f"Basierend auf der folgenden Geschichte, erstelle {anzahl_charaktere} detaillierte Charakterprofile:\n\n{story}"
        '''TO DO API Call richtig schreiben'''
        response = client.completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
        return response.choices[0].text.strip()
    else:
    # Lesen des Prompts aus der Datei mit UTF-8-Kodierung
        with open(file_path, 'r', encoding='utf-8') as file:
            prompt = file.read()

        # Senden des Prompts an GPT-4 und Empfangen der Antwort
        response = client.chat.completions.create(
        model="gpt-4",  # Sie können das gewünschte Modell hier spezifizieren
        messages=[prompt],
        max_tokens=150
    )
    return response.choices[0].text.strip()

