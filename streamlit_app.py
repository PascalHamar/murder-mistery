import streamlit as st

def generate_story():
    # Placeholder for story generation logic
    return "Mystery Story", "Character List"

def main():
    st.title("Murder Mystery Game")

    if st.button("Start Game"):
        story, characters = generate_story()
        st.write("Story: ", story)
        st.write("Characters: ", characters)
    else:
        st.write("Click the button to start the game!")

if __name__ == "__main__":
    main()

