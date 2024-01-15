import time
from openai import OpenAI
import os

# AUTH
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_generated_content_from_prompt(prompt):
    # Send prompt to GPT-4 and receive response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content

# Assistant
# Upload game instructions

file = client.files.create(
    file=open('v3/game_instructions.txt', 'rb'),  # Open the file in binary mode
    purpose='assistants'
    )
# Functions
tools = [{"type": "retrieval"}]

create_characters = {
    "name": "create_characters",
    "description": "A function takes in a number of characters and creates for each character a name, a description and a fact sheet. ",
    "parameters": {
        "type": "object",
        "properties": {
            "name" : {
                "type": "string",
                "description" : "The name of the character. This is the name that will be used in the story. "
            },
            "description": {
                "type": "string",
                "description" : "The description of the character from the narrators perspective to the character e.g. You are ..."

            },
            "factsheet" : {
                "type": "string",
                "description" : "factsheet of the character. This is the information that the player knows about the character. "

            }
        }
    },
    "required": ["name", "description", "factsheet"]
}
tools.append({'type': 'function', 'function': create_characters})
print(tools)

# Add file to assistant
assistant = client.beta.assistants.create(
    name="game_generator",
    instructions="You are a game generator of the given game in game_instructions. You are responsible for generating the game artifacts",
    model="gpt-4-1106-preview",
    tools=tools,
    file_ids=[file.id]
)
print(assistant)

# Create empty thread
thread = client.beta.threads.create()
print(thread)

# Add message to thread
message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = 'user',
    content='Create a murder story with the theme: london. Create 4 characters for that story with 2 hints each. Each character should get 3 information about themselves. Print out the Backstory, the Characters and the resolution of the murder case.'
)
print(message)

# Run assistant
run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id,
)
print(run.id)
# retrieve run status
run = client.beta.threads.runs.retrieve(
    thread_id = thread.id,
    run_id = run.id
)
print(run.status)

while run.status not in ["completed", "failed", "requires_action"]:
  run = client.beta.threads.runs.retrieve(
    thread_id = thread.id,
    run_id = run.id
  )

  print(run.status)
  time.sleep(10)
print(run.status)

# requires action call functions
tools_to_call = run.required_action.submit_tool_outputs.tool_calls
print(len(tools_to_call))
print(tools_to_call)

print(tools_to_call[0].function.name)
print(tools_to_call[0].function.arguments)

tools_output_array = []
for each_tool in tools_to_call:
  tool_call_id = each_tool.id
  function_name = each_tool.function.name
  function_arg = each_tool.function.arguments
  print("Tool ID:" + tool_call_id)
  print("Function to Call:" + function_name )
  print("Parameters to use:" + function_arg)

  if (function_name == 'create_characters'):
    output=True

  tools_output_array.append({"tool_call_id": tool_call_id, "output": output})

print(tools_output_array)

run = client.beta.threads.runs.submit_tool_outputs(
    thread_id = thread.id,
    run_id = run.id,
    tool_outputs=tools_output_array
)

while run.status not in ["completed", "failed", "requires_action"]:
  run = client.beta.threads.runs.retrieve(
    thread_id = thread.id,
    run_id = run.id
  )

  print(run.status)
  time.sleep(10)
print(run.status)

# Retrieve response message from assistant
messages = client.beta.threads.messages.list(
    thread_id = thread.id,

)

for each in messages:
  print(each.role + ":" + each.content[0].text.value)
