import streamlit as st
import gamecontroller as gc

#'ONEPROMPT'
def main():
    st.title("Murder Mystery Game Generator")
    # Initialisation
    if 'game_status' not in st.session_state:
        st.session_state.game_status = 'init'

    # Start Game
    if st.session_state.game_status == 'init':
        "Please enter your configurations:"
        st.session_state.theme = st.text_input("Theme")
        st.session_state.num_characters = st.number_input("Number of characters", min_value=3, max_value=10, step=1)
        st.session_state.num_information = st.number_input("Information per character", min_value=1, max_value=10, step=1)
        st.session_state.num_hints = st.number_input("Hints per character", min_value=1, max_value=10, step=1)
        "Click the button to generate the game!"
        if st.button("Generate Game"):
            st.session_state.generated_content = gc.start_game_one_prompt()
            st.session_state.game_status = 'content_generated'
            st.session_state.generated_content




if __name__ == "__main__":
    main()
