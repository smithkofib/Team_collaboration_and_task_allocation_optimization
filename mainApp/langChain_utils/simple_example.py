#### pip install openai

#from openai import OpenAI
from langchain_community.llms import OpenAI


client = OpenAI(
 #api_key=""
)

completion = client(
  model="gpt-3.5-turbo",
  store=True,
  messages=[
   {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!!"},
  ]
)

print(completion.choices[0].message.content)
