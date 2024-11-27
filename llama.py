from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = InferenceClient(api_key=TOKEN)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.2-1B-Instruct",
    messages=[
        {"role": "system", "content": "Eres el mayor experto en ciberseguridad del mundo."},
        {"role": "user", "content": "¿Crees que los ordenadores cuánticos nos quitaran el trabajo a todos los informaticos?"}
    ],
    max_tokens=150, #controla la longitud del texto generado
    temperature=0.7, #controla la aleatoriedad de las predicciones, valores bajos generan texto más predecible
    top_p=0.9, #limita la probabilidad acumulada de las palabras generadas, evita que se genere texto incoherente
    stop=["user:"]
)


print(completion.choices)