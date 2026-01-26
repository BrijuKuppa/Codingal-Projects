import streamlit as st, os
from google import genai
from google.genai import types
from dotenv import load_dotenv 

load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("api_key"))

# Function to generate AI response
def generate_response(prompt, temperature=0.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=contents, config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
def setup_ui():
    st.title("AI Teaching Assistant")
    st.write("Ask any question. I will provide an answer.")

    user_input = st.text_input("Enter your question:")
    if user_input:
        st.write(f"**Your question:** {user_input}")
        response = generate_response(user_input)
        st.write(f"**AI's answer:** {response}")

def main():
    setup_ui()

if __name__ == "__main__":
    main()
