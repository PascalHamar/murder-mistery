import streamlit as st
from openai import OpenAI
import os
import utils as utils

# AUTH
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

# Storygenerator
def generate_story_from_prompt(file_path):
    # Read prompt from file
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Send prompt to GPT-4 and receive response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content

# Story generator with custom prompt ONEPROMPT
def generate_story_from_custom_prompt(file_path):
    # Read prompt from file
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    prompt = utils.convert_input_to_prompt(prompt, st.session_state.num_characters, '<num_characters>')
    prompt = utils.convert_input_to_prompt(prompt, st.session_state.num_information, '<num_information>')
    prompt = utils.convert_input_to_prompt(prompt, st.session_state.num_hints, '<num_hints>')
    prompt = utils.convert_input_to_prompt(prompt, st.session_state.theme, '<theme>')
    #prompt = utils.convert_input_to_prompt(prompt, st.session_state.custom, '<custom>')

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        max_tokens=2500
    )
    return response.choices[0].message.content

# Character generator
def generate_characters_from_story(story, num_characters):
    prompt = f"Basierend auf der folgenden Geschichte, erstelle {num_characters} detaillierte Charakterprofile:\n\n{story}"
    # Send prompt to GPT and receive response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content