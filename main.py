# impor api key using dotenv
from dotenv import load_dotenv

load_dotenv()

import os
from groq import Groq

client = Groq(
    api_key= os.getenv('GROQ_API_KEY')
)

chat = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': "Explain the what model you are using and how many parameters it has"
        }
    ],
    model= 'llama-3.2-3b-preview'
)

print(chat.choices[0].message.content)