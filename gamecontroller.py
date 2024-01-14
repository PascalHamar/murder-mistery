import storygenerator as sg

def start_game():
    prompt_file = 'test.txt'
    story = sg.generate_story_from_prompt(prompt_file)
    '''PROMPT-DEBUGGING'''
    f = open('story.txt', "w", encoding='utf-8')
    f.write(story)
    f.close()
    return story


def create_characters(story, num_characters):
    characters = sg.generate_characters_from_story(story, num_characters)
    '''PROMPT-DEBUGGING'''
    f = open('characters.txt', "w", encoding='utf-8')
    f.write(characters)
    f.close()
    return characters

def start_game_one_prompt():
    prompt_file = 'prompt_v2.txt'
    generated_story = sg.generate_story_from_custom_prompt(prompt_file)
    return generated_story
