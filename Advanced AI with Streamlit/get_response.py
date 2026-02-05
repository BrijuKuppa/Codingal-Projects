import streamlit as st, json, os
from dotenv import load_dotenv
from google import genai
from flask import Flask, request, jsonify, render_template

load_dotenv()
app = Flask(__name__)

memory = []

client = genai.Client(api_key=os.getenv("api_key"))
def generate(prompt):
    try: return client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
        ).text
    except Exception as e: return f"Something went wrong... (Debug: {e})"

@app.route("/")
def render():
    return render_template("index.html")

@app.route("/generate", methods=["GET", "POST"])
def main():
    prompt = f"Memory: {memory}, Prompt: {request.json}."
    output = jsonify({"reply" : generate(prompt)})
    memory.append({"prompt" : prompt, "response" : output})

    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)