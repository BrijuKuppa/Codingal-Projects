import requests
from config import HF_API_KEY
import re

HF_API_Key = "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"


def find_sentiment(text):
    url = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

    headers = {"Authorization" : f"Bearer {HF_API_KEY}"}
    payload = {"inputs" : text}
    output = requests.post(url, headers=headers, json=payload)

    if output.status_code != 200:
        return output.status_code
    
    return output.json()

def user_input():
    print("\n\nThis is a sentiment predictor. Please type a sentence to get started. (To start a new line, type like this: '{sentence goes here}. {new sentnece starts here.})'")

    user_input = input("Type away... ")


    # Failed Code
    # key = 1
    # i_dictionary = {"sentence1": ""}
    # for i, sen in enumerate(user_input):
    #     if sen == "." or sen == "?" or sen == "!":
    #         key += 1
    #         i_dictionary[f"sentence{key}"] = sen
    #         continue
    #     i_dictionary[f"sentence{key}"] += sen

    # if len(i_dictionary) == 1:
    #         if key == 1:
    #             key = 1
    #         elif key != 1:
    #             key = key - 1

    # for i in range(1, key):
    #     print("\nResults:")
    #     print(i_dictionary[f"sentence{i}"])
    #     print(find_sentiment(i_dictionary[f"sentence{i}"]))



    sentences = re.split(r'(?<=[.!?])\s+', user_input.strip())

    print("\nResults:")
    for sentence in sentences:
        if sentence.strip():
            print(f"\nSentence: {sentence}")
            print(find_sentiment(sentence))

if __name__ == "__main__":
    user_input()
