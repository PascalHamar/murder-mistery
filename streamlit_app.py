import streamlit as st
import storygenerator as sg

def generate_story():
    sg.main()

def main():
    st.title("Murder Mystery Game")

    if st.button("Start Game"):
        st.write("Content: ", generate_story())
    else:
        st.write("Click the button to start the game!")

if __name__ == "__main__":
    main()

