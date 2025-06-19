#from openai import OpenAI
import os
import openai
#client = OpenAI()
#openai.api_key = ""
completion = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": "what is a dog"
    }]
)

print(completion.choices[0].message.content)
