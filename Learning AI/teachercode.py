# # Install required library (run once)
# # !pip install transformers torch

# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # Load pre-trained GPT-2 model and tokenizer
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

# # Function to generate response
# def get_response(prompt, max_length=80):
#     inputs = tokenizer.encode(prompt, return_tensors="pt")
#     outputs = model.generate(
#         inputs,
#         max_length=max_length,
#         num_return_sequences=1,
#         pad_token_id=tokenizer.eos_token_id
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return response

# print(get_response("""
# Q: What are the benefits of reading?

# A: Reading improves knowledge, vocabulary, and concentration.

# Q: What are the benefits of exercise?

# A: Exercising can make you healthy and fit, making you more athletic as well.
# """))















import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------------
# ZERO-SHOT EXAMPLES
# -------------------------------

def zero_shot():
    print("\n--- ZERO SHOT ---")

    prompt = """
    Classify the sentiment as Positive, Negative, or Neutral.

    Sentence: "I waited for an hour, but the service was excellent."
    """

    response = model.generate_content(prompt)
    print("Sentiment:", response.text)

    quote_prompt = "Write a motivational quote about hard work."
    response = model.generate_content(quote_prompt)
    print("Quote:", response.text)


# -------------------------------
# ONE-SHOT EXAMPLES
# -------------------------------

def one_shot():
    print("\n--- ONE SHOT ---")

    prompt = """
    Example:
    Sentence: "The movie was boring."
    Sentiment: Negative

    Now classify:
    Sentence: "The food was delicious."
    Sentiment:
    """

    response = model.generate_content(prompt)
    print("Sentiment:", response.text)

    quote_prompt = """
    Example:
    Topic: Time
    Quote: Time waits for no one, so use it wisely.

    Now write a quote on Success:
    """

    response = model.generate_content(quote_prompt)
    print("Quote:", response.text)


# -------------------------------
# FEW-SHOT EXAMPLES
# -------------------------------

def few_shot():
    print("\n--- FEW SHOT ---")

    prompt = """
    Sentence: "The app keeps crashing."
    Sentiment: Negative

    Sentence: "Customer support solved my issue quickly."
    Sentiment: Positive

    Sentence: "The product arrived on time."
    Sentiment: Neutral

    Now classify:
    Sentence: "The battery life is terrible."
    Sentiment:
    """

    response = model.generate_content(prompt)
    print("Sentiment:", response.text)

    quote_prompt = """
    Topic: Discipline
    Quote: Discipline turns goals into habits.

    Topic: Knowledge
    Quote: Knowledge grows when shared.

    Topic: Patience
    Quote:
    """

    response = model.generate_content(quote_prompt)
    print("Quote:", response.text)


# -------------------------------
# MAIN FUNCTION
# -------------------------------

if __name__ == "__main__":
    zero_shot()
    one_shot()
    few_shot()