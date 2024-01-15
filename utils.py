# Description: This file contains utility functions that are used in the main script.

# Function that converts the inputs and replace the placeholders in the prompt file
def convert_input_to_prompt(file, input, var_name):
    file = file.replace(var_name, str(input))
    return file