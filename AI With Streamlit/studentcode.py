from dotenv import load_dotenv; from google import genai; import streamlit as st, os

load_dotenv()

conversation_history = []

client = genai.Client(api_key=os.getenv("api_key"))
def generate(prompt: str, memory=False):
    try:
        return client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Memory:{memory}. Prompt:{prompt.strip()}" if memory else prompt.strip()
            ).text
    except Exception as e:
        return f"Oopsies! Lets see what happened: {e}"
    
def main():
    st.title("AI Essay Helper")
    st.write("Lets work on your essays.")

    if prompt := st.chat_input("Type away..."):
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            output = generate(prompt, memory=conversation_history)
            st.markdown(output)

            conversation_history.append({"user" : prompt, "assistant" : output}) 
        
    st.write("AI-generated content is provided for informational purposes only and may contain errors or inaccuracies. Do not rely on it as a sole source of truth.")


if __name__ == "__main__":
    main()