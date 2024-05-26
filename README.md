# 20 Questions game with LLM

This project build during the Mistral LLM Hackathon 2024.

The idea to test LLMs with 20 Questions game and try to fine-tune LLMs with synthetically generated data.

## Dataset

New dataset [Q20LLM](https://huggingface.co/datasets/cvmistralparis/) was created and uploaded to Huggingface.

## Evaluation

Evaluation scripts was taken from [Entity-Deduction Arena (EDA)](https://github.com/apple/ml-entity-deduction-arena) project.


| Model        |    #Turns (↓)   | Success (↑) |    #Yes     | Score (↑) |
|--------------|:------------------:|:---------:|:-------------:|:--------:|
| open-mistral-7b | 18.97 | 0.14 | 4.52 | 0.1186 |
| mistral-7B-Instruct-v0.3 | 19.06 | 0.15 | 4.47 | 0.1238 |
| open-mixtral-8x7b | 18.57 | 0.21 | 5.81 | 0.1756 |
| mistral-small-latest | 18.18 | 0.25 | 5.65 | 0.2114 |
| open-mixtral-8x22b | 17.92 | 0.31 | 5.38 | 0.2586 |
| mistral-medium-latest | 17.97 | 0.29 | 5.56 | 0.2436 |
| mistral-large-latest | 17.92 | 0.32 | 6.5 | **0.2656** |