import os
import openai

# Load API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Ctrl-c or enter 'exit!' to terminate.\n")
messages = []

while True:
    # Input prompt
    prompt = input("User: ")

    # Check if user wants to exit
    if (prompt == 'exit!'):
        break

    # Append the message as 'user'
    messages.append({
        "role": "user",
        "content": prompt})

    # Generate completion
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    # Print out response, and then save the response as 'assistant'
    response = completion.choices[0].message.content
    print(f'ChatGPT: {response}')
    messages.append({"role": "assistant", "content": response})
