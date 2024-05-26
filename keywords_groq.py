import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

seed = 14

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert in the 20 Questions deduction game.",
        },
        {
            "role": "user",
            "content": """Generate a list of 500 diverse and simple keywords suitable for the 20 Questions game. Ensure the keywords cover a broad range of categories including but not limited to: animals, culture, science, geography, time, people, government, education, family, health, economy, nature, technology, entertainment, history, sports, art, music, literature, food, travel, religion, fashion, politics, transportation, environment, emotions, hobbies, tools, architecture, and more.""",
        }
    ],
    model="llama3-70b-8192",
    temperature=1,
    max_tokens=4000,
    seed=seed,
)

completion = chat_completion.choices[0].message.content

with open(f"data/keywords/llama3-70b-8192/{seed}.txt", "w") as file:
    file.write(completion)
