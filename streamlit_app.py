import streamlit as st
import gamecontroller as gc


def main():
    st.title("Murder Mystery Game Generator")
    # Initialisation
    if 'game_status' not in st.session_state:
        st.session_state.game_status = 'init'

    # Start Game
    if st.session_state.game_status == 'init':
        "Click the button to generate the game!"
        if st.button("Generate Game"):
            st.session_state.gamestory = gc.start_game()
            st.session_state.game_status = 'story'


    # Gameconfiguration
    if st.session_state.game_status == 'story':
        st.write(st.session_state.gamestory)
        num_characters = st.number_input("Enter the number of players/characters:", min_value=3, max_value=10, step=1)

        if st.button("Submit"):
            st.session_state.characters = gc.create_characters(st.session_state.gamestory, num_characters)
            st.session_state.game_status = 'characters'

    # Display characters
    if st.session_state.game_status == 'characters':
        st.write(st.session_state.characters)


if __name__ == "__main__":
    main()
