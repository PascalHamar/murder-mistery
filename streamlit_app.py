import streamlit as st
import storygenerator as sg


def main():
    st.title("Murder Mystery Game")

    if st.button("Start Game"):
        # Hier geben Sie den Pfad zur Datei an, die den Prompt enthält
        prompt_file = 'storyprompt.txt'
        story = sg.generate_story_from_prompt(prompt_file)
        st.write("Story: ", story)
    else:
        st.write("Click the button to start the game!")

if __name__ == "__main__":
    main()
