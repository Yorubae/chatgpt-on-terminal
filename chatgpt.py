# Uhmm A simple script that uses the openai wrapper
# You can use it however you want

# Author : Yoru
# Insta : soooricky
# twitter : chimshoubae
# Github : Yorubae


import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ["apiID"]
model = "gpt-3.5-turbo"
print("Chatgpt enterned the chat!")
while True:
    try:
        query = input("You: ")
        if query == "exit":
            break
        response = openai.ChatCompletion.create(
            api_key=api_key,
            model=model,
            messages=[
                {"role": "system", "content": "Say hello to chatgpt!"},
                {"role": "user", "content": query},
            ],
        )
        print(f"Chatgpt: {response['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"Error: {e}")

print("Quiting")
