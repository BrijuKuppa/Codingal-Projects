import os, time; from google import genai

os.environ["api_key"] = input("\nEnter your Gemini API key here:"); client = genai.Client(api_key=os.environ["api_key"])
def generate(prompt: str): 
    try: return client.models.generate_content(model="gemini-3-flash-preview", contents=prompt).text 
    except Exception as e: print(f"\n{e}")

def main():
    print("\n\nWelcome to Zero/One/Few Shot Learning!\n- Examine the prompt and response, and think about what you notice.\n- More info is given below the response.\n\nZero Shot Learning:\n- Prompt: Classify the sentiment as Positive, Negative, or Neutral. Sentence: 'I waited for an hour, but the service was excellent.'")
    print(f"- Output: {generate("Classify the sentiment as Positive, Negative, or Neutral. Sentence: 'I waited for an hour, but the service was excellent.'")}\n- With zero examples, the AI will give a less acurate output.")
    time.sleep(5)
    print(f"\n\nOne Shot Learning:\n- Prompt: Example: Sentence: 'The movie was boring.' Sentiment: Negative Now classify: Sentence: 'The food was delicious.' Sentiment:\n- Output: {generate("Example: Sentence: 'The movie was boring.' Sentiment: Negative Now classify: Sentence: 'The food was delicious.' Sentiment:")}\n- With one example, the AI will give more of an accurate output.")
    time.sleep(5)  
    print(f"\n\nFew Shot Learning:\n- Prompt: Sentence: 'The app keeps crashing.' Sentiment: Negative | Sentence: 'Customer support solved my issue quickly.' Sentiment: Positive | Sentence: 'The product arrived on time.' Sentiment: Neutral | Now classify: Sentence: 'The battery life is terrible.' Sentiment:\n- Output: {generate("Sentence: 'The app keeps crashing.' Sentiment: Negative | Sentence: 'Customer support solved my issue quickly.' Sentiment: Positive | Sentence: 'The product arrived on time.' Sentiment: Neutral | Now classify: Sentence: 'The battery life is terrible.' Sentiment:")}\n- With multiple examples, the AI will give a better output than the last.")

if __name__ == "__main__":
    main()