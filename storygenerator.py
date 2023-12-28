from openai import OpenAI

client = OpenAI()

def send_prompt_to_gpt4(file_path):
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

def save_response_to_file(response, file_path):
    # Speichern der Antwort in einer Datei mit UTF-8-Kodierung
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response)

# Hauptausführung
if __name__ == "__main__":
    prompt_file = 'storyprompt.txt'
    response_file = 'response.txt'

    response = send_prompt_to_gpt4(prompt_file)
    save_response_to_file(response, response_file)
    print("Antwort in " + response_file + " gespeichert.")

