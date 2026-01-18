from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("api_key"))

def generate(prompt, temp=0.5):
    try:
        return client.models.generate_content(
            model="gemini-3.0-flash-preview", 
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
            config=types.GenerateContentConfig(temperature=temp)
            ).text
    except Exception as e:
        return f"Oh no! Let's see what happened: {e}"
    
if __name__ == "__main__":
    print("Gemini")