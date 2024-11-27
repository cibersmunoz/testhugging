import requests
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2.1-1B"
headers = {"Authorization": f"Bearer {TOKEN}"}
payload = {
    "inputs": "Fuimos Alvaro y yo a la aceituna con pila perras...",
    "parameters":{
        "max_new_tokens": 300,
        "temperature": 1.0,
        "repetition_penalty": 1.5,
    }
}


response = requests.post(API_URL, headers=headers, json=payload)
response.json()

print(response.json())