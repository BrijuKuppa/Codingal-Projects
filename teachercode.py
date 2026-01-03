# Install Gemini SDK

import os
import time
from getpass import getpass
from google import genai
from google.genai import types

# Set your Gemini API key securely
# Enter your key when prompted (it won't show in output)
os.environ["GEMINI_API_KEY"] = getpass("Enter your Gemini API Key: ")

def generate_response(prompt, temperature=0.5):
    """Generate a response from Gemini API with a specified temperature."""
    try:
        # Initialize the client using the environment variable
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

        # Create the content structure
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]

        # Configure generation parameters
        generate_content_config = types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )

        # Generate content
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=generate_content_config,
        )
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def temperature_prompt_activity():
    """Interactive activity to explore temperature settings and instruction-based prompts."""
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)

    base_prompt = input("\nEnter a creative prompt: ")
    print("\nGenerating responses with different temperatures...\n")

    for temp in [0.1, 0.5, 0.9]:
        print(f"\n--- TEMPERATURE {temp} ---")
        print(generate_response(base_prompt, temperature=temp))
        time.sleep(1)

    topic = input("\nChoose a topic: ")
    instructions = [
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}.",
    ]

    for i, instruction in enumerate(instructions, 1):
        print(f"\n--- INSTRUCTION {i}: {instruction} ---")
        print(generate_response(instruction, temperature=0.7))
        time.sleep(1)

    custom_instruction = input("\nEnter your own instruction-based prompt: ")
    try:
        custom_temp = float(input("\nSet a temperature (0.1 to 1.0): "))
        if not 0.1 <= custom_temp <= 1.0:
            custom_temp = 0.7
    except ValueError:
        custom_temp = 0.7

    print(f"\n--- YOUR PROMPT WITH TEMPERATURE {custom_temp} ---")
    print(generate_response(custom_instruction, temperature=custom_temp))

# Run the activity
temperature_prompt_activity()
































import os
import time
from getpass import getpass
from google import genai
from google.genai import types


# ------------------------------------------------------------
# FUNCTION: Generate a response from Gemini at a given temperature
# ------------------------------------------------------------
def generate_response(prompt, temperature=0.5):
    """Generate a response from Gemini API with custom temperature."""
    try:
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]

        config = types.GenerateContentConfig(
            temperature=temperature,
            response_mime_type="text/plain",
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config,
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"


# ------------------------------------------------------------
# MAIN ACTIVITY: Prompt Lab
# ------------------------------------------------------------
def prompt_lab():
    print("=" * 80)
    print("🎨 PROMPT LAB: TUNE YOUR CREATIVITY & CONTROL")
    print("=" * 80)

    # Ask user for their Gemini API key
    os.environ["GEMINI_API_KEY"] = getpass("Enter your Gemini API Key: ")

    # STEP 1: Temperature exploration
    print("\nSTEP 1: Temperature Tuning")
    base_prompt = input("\nEnter a creative prompt: ")

    for temp in [0.1, 0.5, 0.9]:
        print(f"\n--- TEMPERATURE = {temp} ---")
        print(generate_response(base_prompt, temperature=temp))
        time.sleep(1)

    # STEP 2: Instruction-Based Prompting
    print("\n" + "=" * 80)
    print("STEP 2: Instruction-Based Prompting")
    print("=" * 80)

    topic = input("\nEnter a topic: ")

    tasks = [
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I am 10 years old.",
        f"Give a pro/con list about {topic}.",
        f"Write a fictional headline from 2050 related to {topic}.",
    ]

    for i, task in enumerate(tasks, 1):
        print(f"\n--- TASK {i}: {task} ---")
        print(generate_response(task, temperature=0.7))
        time.sleep(1)

    # STEP 3: Custom Experiment
    print("\n" + "=" * 80)
    print("STEP 3: Your Experiment")
    print("=" * 80)

    custom_prompt = input("\nEnter your custom instruction prompt: ")

    try:
        temp = float(input("Choose a temperature (0.1 to 1.0): "))
        if not 0.1 <= temp <= 1.0:
            temp = 0.7
    except:
        temp = 0.7

    print(f"\n--- CUSTOM OUTPUT at temperature {temp} ---")
    print(generate_response(custom_prompt, temperature=temp))


# Run the activity
prompt_lab()
