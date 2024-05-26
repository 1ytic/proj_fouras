import os
import pandas as pd
from tqdm import tqdm
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def load_apple_keywords():
    keywords = set()
    with open("ml-entity-deduction-arena/data/things/newlist_things.rmdup.dev.txt", "r") as f:
        for line in f.read().splitlines():
            words = line.strip().split(" | ")
            keywords.update(words)
    return keywords


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

template = """Generate 20 insightful and strategic questions designed to help identify the word '{KEYWORD}'. Try to deduce the word by narrowing their questions from general to specific, in hopes of guessing the word in the fewest number of questions. For each question provide answer "yes" or "no". You must provide only 5 "yes" answers. Ensure that each question focuses on a single attribute or feature. Compose your question without using the conjunction 'or'. Try to make questions short. Output result without explanation and start directly from the questions list. Use the following format:

1. Question 1? Yes
2. Question 2? No"""

completions = []

model_name = "llama3-70b-8192"

all_keywords = set(pd.read_csv("data/keywords_all3.csv").keyword.tolist())
# all_keywords = load_apple_keywords()

existing_keywords = set()
folder = f"data/questions/{model_name}-20"
total_files = 1
for name in os.listdir(folder):
    existing_keywords.update(pd.read_csv(f"{folder}/{name}").keyword.tolist())
    total_files += 1

keywords = sorted(all_keywords - existing_keywords)

keywords = sorted(all_keywords)
keywords = [k for k in keywords if " " not in k]

for keyword in tqdm(keywords):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert in the 20 Questions deduction game.",
            },
            {
                "role": "user",
                "content": template.format(KEYWORD=keyword),
            }
        ],
        model=model_name,
        temperature=0.5,
        max_tokens=512,
        stop="\n21.",
        seed=37,
    )
    completions.append({
        "keyword": keyword,
        "completion": chat_completion.choices[0].message.content,
    })
    if len(completions) % 10 == 0:
        pd.DataFrame(completions).to_csv(f"data/questions/{model_name}-20/{total_files}.csv", index=False)