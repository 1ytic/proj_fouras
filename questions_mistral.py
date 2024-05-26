import os
import pandas as pd
from tqdm import tqdm
from mistralai.client import MistralClient
from dotenv import load_dotenv

load_dotenv()

client = MistralClient(api_key=os.environ["MISTRAL_API_KEY"])

template = """Generate 10 insightful and strategic questions designed to help identify the word '{KEYWORD}'. Try to deduce the word by narrowing their questions from general to specific, in hopes of guessing the word in the fewest number of questions. For each question provide answer "yes" or "no". Ensure your list includes both "yes" and "no" answers. Ensure that each question focuses on a single attribute or feature. Compose your question without using the conjunction 'or'. Try to make questions short. Output result without explanation and start directly from the questions list. Use the following format:

1. Question 1? Yes
2. Question 2? No"""

completions = []

keywords = pd.read_csv("data/keywords_all.csv").keyword.tolist()

for keyword in tqdm(keywords):
    messages = [
        {
            "role": "system",
            "content": "You are an expert in the 20 Questions deduction game.",
        },
        {
            "role": "user",
            "content": template.format(KEYWORD=keyword),
        }
    ]
    stream_response = client.chat_stream(
        model="mistral-large-latest",
        messages=messages,
        max_tokens=256,
        temperature=0.5,
        random_seed=2,
    )
    completion = ""
    for chunk in stream_response:
        completion += chunk.choices[0].delta.content
        if "\n11." in completion:
            completion = completion.split("\n11.")[0]
            break
    completions.append({
        "keyword": keyword,
        "completion": completion,
    })
    if len(completions) % 10 == 0:
        pd.DataFrame(completions).to_csv("data/questions/mistral-large-latest/2.csv", index=False)