# =======================================
# 🤖 AI Text Summarizer (Google Colab)
# Using Hugging Face Inference API
# =======================================

# STEP 1: Install required packages
# !pip install colorama requests --quiet

# STEP 2: Set your Hugging Face API Key
# ⚠️ Replace with your actual API key from https://huggingface.co/settings/tokens
API_KEY = "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"

# STEP 3: Import libraries
import requests
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ---------------------------
# Default Config
# ---------------------------
DEFAULT_MODEL = "google/pegasus-xsum"#summization

if not API_KEY or API_KEY.startswith("hf_your"):
    print(Fore.RED + "❌ Please set your Hugging Face API key in API_KEY above before running.")
else:
    print(Fore.GREEN + "✅ API Key loaded successfully.")


# ---------------------------
# Build API URL
# ---------------------------
def build_api_url(model_name: str) -> str:
    return f"https://api-inference.huggingface.co/models/{model_name}"


# ---------------------------
# Query API
# ---------------------------
def query_api(payload: dict, model_name: str = DEFAULT_MODEL) -> dict:
    url = build_api_url(model_name)
    headers = {"Authorization": f"Bearer {API_KEY}"}

    for attempt in range(3):  # retry logic if model is loading
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 503:  # Model still loading
            print(Fore.YELLOW + "⏳ Model is loading... retrying in 5 seconds")
            time.sleep(5)
        else:
            print(Fore.RED + f"❌ API Error: {response.status_code} - {response.text}")
            return None
    return None


# ---------------------------
# Summarization Function
# ---------------------------
def summarize_text(text: str, min_len: int, max_len: int, model_name: str = DEFAULT_MODEL):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_len,
            "max_length": max_len,
        },
    }

    print(Fore.CYAN + f"\n🔄 Summarizing with model: {model_name} ...")
    response = query_api(payload, model_name)

    if not response:
        return None

    if isinstance(response, list) and "summary_text" in response[0]:
        return response[0]["summary_text"]
    else:
        print(Fore.RED + f"❌ Unexpected response: {response}")
        return None


# ---------------------------
# Main Execution
# ---------------------------
def run_summarizer():
    print(Fore.GREEN + "🤖 Welcome to AI Summarizer!")

    user_name = input("Enter your name: ").strip() or "User"
    print(Fore.YELLOW + f"Hello, {user_name} 👋")

    text = input("\nEnter the text you want to summarize:\n").strip()
    if not text:
        print(Fore.RED + "❌ No input text provided. Exiting...")
        return

    model_name = input(f"\nEnter model name (or press Enter to use default '{DEFAULT_MODEL}'): ").strip() or DEFAULT_MODEL

    print(Fore.MAGENTA + "\nChoose summarization style:")
    print("1️⃣  Standard Summary (Concise)")
    print("2️⃣  Enhanced Summary (Detailed)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        min_len, max_len = 20, 60
    elif choice == "2":
        min_len, max_len = 50, 150
    else:
        print(Fore.RED + "❌ Invalid choice. Defaulting to Standard Summary.")
        min_len, max_len = 20, 60

    summary = summarize_text(text, min_len, max_len, model_name)

    if summary:
        print(Fore.GREEN + "\n✅ Summary Generated:")
        print(Fore.WHITE + Style.BRIGHT + summary)
    else:
        print(Fore.RED + "❌ Failed to generate summary.")


# Run the summarizer
if API_KEY and not API_KEY.startswith("hf_your"):
    run_summarizer()
