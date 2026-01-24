# Step 2: Import libraries
import os
from google import genai
from google.genai import types
from colorama import init, Fore

# Initialize colorama for colored output
init(autoreset=True)

os.environ["GEMINI_API_KEY"] = "AIzaSyAyL0mBKD0cX8HhQY2l8zDrARe_wJioDcU"

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Please set your GEMINI_API_KEY in the environment.")

# Step 5: Initialize Gemini client
client = genai.Client(api_key=API_KEY)
print(Fore.GREEN + "✅ Gemini client initialized successfully")

def get_essay_details():
    print(Fore.CYAN + "\n=== AI Writing Assistant ===\n")

    topic = input(Fore.YELLOW + "What is the topic of your essay? ")
    essay_type = input(Fore.YELLOW + "What type of essay are you writing? (e.g., Argumentative, Expository, Descriptive) ")

    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print("1. 300 words\n2. 900 words\n3. 1200 words\n4. 2000 words")
    word_count_choice = input(Fore.YELLOW + "Enter choice number: ")
    word_count_dict = {"1": "300", "2": "900", "3": "1200", "4": "2000"}
    length = word_count_dict.get(word_count_choice, "300")

    target_audience = input(Fore.YELLOW + "Who is the target audience? ")
    specific_points = input(Fore.YELLOW + "Any specific points to include? ")
    stance = input(Fore.YELLOW + "What is your stance? (For/Against/Neutral) ")
    references = input(Fore.YELLOW + "Any references or sources? ")
    writing_style = input(Fore.YELLOW + "Preferred writing style? (Formal/Conversational/etc.) ")
    outline_needed = input(Fore.YELLOW + "Do you want an outline first? (Yes/No) ").lower()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience,
        "specific_points": specific_points,
        "stance": stance,
        "references": references,
        "writing_style": writing_style,
        "outline_needed": outline_needed
    }

def generate_essay_content(details):
    temperature = float(input(Fore.YELLOW + "Enter temperature (0.2 structured → 0.7 creative): "))

    # Introduction
    intro_prompt = f"Write an introduction for a {details['essay_type']} essay on {details['topic']} with stance {details['stance']}."
    introduction = generate_response(intro_prompt, temperature)
    print(Fore.CYAN + "\n=== Introduction ===")
    print(Fore.GREEN + introduction)

    # Body
    body_style = input(Fore.YELLOW + "Body style? (Step-by-step/Full draft): ").lower()
    if body_style == "full draft":
        body_prompt = f"Write a detailed {details['essay_type']} essay about {details['topic']} with stance {details['stance']} in about {details['length']} words."
        body = generate_response(body_prompt, temperature)
        print(Fore.CYAN + "\n=== Full Body ===")
        print(Fore.GREEN + body)
    else:
        body_step_prompt = f"Write structured step-by-step arguments with evidence for an essay on {details['topic']} with stance {details['stance']}."
        body_step = generate_response(body_step_prompt, temperature)
        print(Fore.CYAN + "\n=== Step-by-Step Body ===")
        print(Fore.GREEN + body_step)

    # Conclusion
    conclusion_prompt = f"Write a conclusion for a {details['essay_type']} essay about {details['topic']} with stance {details['stance']}."
    conclusion = generate_response(conclusion_prompt, temperature)
    print(Fore.CYAN + "\n=== Conclusion ===")
    print(Fore.GREEN + conclusion)

def feedback_and_refinement():
    satisfaction = input(Fore.YELLOW + "Rate satisfaction (1 to 5): ")
    if satisfaction != "5":
        feedback = input(Fore.YELLOW + "What should be improved (tone, structure, depth, etc.)? ")
        print(Fore.CYAN + f"\nThanks. Refinement note: {feedback}")
    else:
        print(Fore.CYAN + "\nEssay is good as is.")

def run_activity():
    print(Fore.CYAN + "\nWelcome to the AI Writing Assistant!")
    details = get_essay_details()
    generate_essay_content(details)
    feedback_and_refinement()

# Run
run_activity()