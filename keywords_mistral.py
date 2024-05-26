import os
from mistralai.client import MistralClient
from dotenv import load_dotenv

load_dotenv()

client = MistralClient(api_key=os.environ["MISTRAL_API_KEY"])

seed = 3

messages = [
    {
        "role": "system",
        "content": "You are an expert in the 20 Questions deduction game.",
    },
    {
        "role": "user",
        "content": """Generate a list of 500 diverse and effective keywords suitable for the 20 Questions game. Ensure the keywords cover a broad range of categories including but not limited to: time, people, government, education, family, health, economy, nature, technology, culture, entertainment, history, science, geography, sports, art, music, literature, food, travel, religion, fashion, politics, transportation, environment, animals, emotions, hobbies, tools, architecture, and more.""",
    }
]

stream_response = client.chat_stream(
    model="mistral-large-latest",
    messages=messages,
    random_seed=seed,
    temperature=0.5,
    max_tokens=4096,
)

with open(f"data/keywords/mistral-large-latest/{seed}.txt", "w") as file:
    for chunk in stream_response:
        file.write(chunk.choices[0].delta.content)
        file.flush()
