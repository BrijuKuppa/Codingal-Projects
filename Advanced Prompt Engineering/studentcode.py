import time, os, gradio as gr
from getpass import getpass
from google import genai
from google.genai import types

os.environ["api_key"] = input("To start the programe, please enter your Google Genai API key. > ")
client = genai.Client(api_key=os.environ["api_key"])

def generate(prompt, temp=0.5):
    try:
        return client.models.generate_content(
                model="gemini-3-flash-preview", 
                contents=prompt, 
                config=types.GenerateContentConfig(
                    temperature=temp, 
                    response_mime_type="text/plain")).text
    except Exception as e:
        return e


def events(text, history):
    temps = ("0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1")

    if "hi" in text.lower() or "hello" in text.lower() or "hey" in text.lower():
        return "Hey! I'm your chatbot helping you with prompt engineering using temperatures. Type a prompt, and put the temperature right after the sentence (Like this: Tell me about doctors. 0.8)."

    elif any(item in text.lower() for item in temps):
        temp = list(filter(lambda item: item in text.lower(), temps))
        prompt = text.replace(temp[0], "")

        return generate(prompt, temp=float(temp[0]))
    
    else:
        return generate(text)
    
gr.ChatInterface(
    events,
    title="Prompt Engineering with Temperature",
    examples=["Tell me about doctors. 0.8", "Hello", "What are seahorses? 0.2"]
).launch(theme="ocean")