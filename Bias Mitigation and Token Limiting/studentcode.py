from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("api_key"))
def generate(prompt, temp=0.5):
    try:
        return client.models.generate_content(
            model="gemini-3.0-lite-preview",
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
            config=types.GenerateContentConfig(temperature=temp)
        )
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    print("\n\nWelcome!\n")

    prompt = input("\nLets start with bias-mitigation: Enter a prompt with bias. > ")
    print(f"Output: {generate(prompt, temp=0.7)}")

    prompt = input("\nNow enter a prompt without bias. > ")
    print(f"Output: {generate(prompt, temp=0.7)}")

    print("-------------------------------------")

    prompt = input("\nLets continue with token limitation: Enter a long prompt. > ")
    print(f"Output: {generate(prompt[:500], temp=0.7)}")

    prompt = input("\nNow enter a shorter prompt. > ")
    print(f"Output: {generate(prompt[:150], temp=0.7)}")

    print("-------------------------------------")

    print("\nBye!")

if __name__ == "__main__":
    main()