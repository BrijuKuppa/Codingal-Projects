# ----------------------------------------------
# AI Prompt Engineering Interactive Tutorial
# Step-by-Step Program (Works with Google Gemini)
# ----------------------------------------------

# Import Google Gemini client
from google import genai       # If using Google Gemini
import config                  # Your config.py must contain GEMINI_API_KEY

# If using OpenAI GPT instead:
# from openai import OpenAI
# client = OpenAI(api_key=config.OPENAI_API_KEY)


# ----------------------------------------------
# Initialize AI Client
# ----------------------------------------------
client = genai.Client(api_key=config.GEMINI_API_KEY)#AIzaSyCoeFjAFJbwL1mUMA_vnfzNwfykOU9xaQA
#import os
#API_KEY = os.getenv("GEMINI_API_KEY")
#client = genai.Client(api_key=API_KEY)AIzaSyCoeFjAFJbwL1mUMA_vnfzNwfykOU9xaQA


# ----------------------------------------------
# Function to Generate AI Response
# ----------------------------------------------
def generate_response(prompt):
    """
    Sends the prompt to the AI model and returns the response text.
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",      # Change if required
        contents=prompt
    )

    return response.text# add try/except


# ----------------------------------------------
# Interactive Prompt Engineering Tutorial
# ----------------------------------------------
def silly_prompt():
    print("\n==============================")
    print(" AI Prompt Engineering Tutorial")
    print("==============================\n")

    print("In this activity, you will learn:")
    print("1. How vague prompts produce weak responses.")
    print("2. How specific prompts improve quality.")
    print("3. How adding context produces the best results.\n")

    print("Let's begin!\n")


    # ----------------------------------------------
    # STEP 1: Create a Vague Prompt
    # ----------------------------------------------
    vague_prompt = input("Step 1 → Enter a vague prompt (e.g., 'Tell me about technology'): ")

    print(f"\nYour vague prompt: {vague_prompt}")
    vague_response = generate_response(vague_prompt)

    print("\nAI's response to the vague prompt:")
    print("----------------------------------")
    print(vague_response)


    # ----------------------------------------------
    # STEP 2: Make the Prompt Specific
    # ----------------------------------------------
    specific_prompt = input("\nStep 2 → Make your prompt more specific "
                            "(e.g., 'Explain how AI works in self-driving cars'): ")

    print(f"\nYour specific prompt: {specific_prompt}")
    specific_response = generate_response(specific_prompt)

    print("\nAI's response to the specific prompt:")
    print("--------------------------------------")
    print(specific_response)


    # ----------------------------------------------
    # STEP 3: Add Context to the Prompt
    # ----------------------------------------------
    contextual_prompt = input("\nStep 3 → Add meaningful context "
                              "(e.g., 'Given the advancements in autonomous vehicles, "
                              "explain how AI is used in self-driving cars to make real-time driving decisions'): ")

    print(f"\nYour contextual prompt: {contextual_prompt}")
    contextual_response = generate_response(contextual_prompt)

    print("\nAI's response to the contextual prompt:")
    print("----------------------------------------")
    print(contextual_response)


    # ----------------------------------------------
    # REFLECTION QUESTIONS
    # ----------------------------------------------
    print("\n==============================")
    print(" Reflection Questions")
    print("==============================")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which version of the prompt gave the best response? Why?\n")


# ----------------------------------------------
# Run the Interactive Tutorial
# ----------------------------------------------
silly_prompt()
















# # ----------------------------------------------
# # AI Prompt Engineering Interactive Tutorial
# # Using Google Gemini
# # ----------------------------------------------

# from google import genai

# # Insert your regenerated API key here
# API_KEY = "AIzaSyCslz4Z3QlArt5-pqDXDwKzsrce6tl-D9c"

# # Initialize client
# client = genai.Client(api_key=API_KEY)


# # ----------------------------------------------
# # Function to Generate AI Response
# # ----------------------------------------------
# def generate_response(prompt):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=prompt
#     )
#     return response.text


# # ----------------------------------------------
# # Interactive Prompt Engineering Tutorial
# # ----------------------------------------------
# def silly_prompt():
#     print("\n==============================")
#     print(" AI Prompt Engineering Tutorial")
#     print("==============================\n")

#     print("In this activity, you will learn:")
#     print("1. How vague prompts produce weak responses.")
#     print("2. How specific prompts improve quality.")
#     print("3. How adding context produces the best results.\n")

#     print("Let's begin!\n")

#     # ------------------------------------------
#     # STEP 1: Vague Prompt
#     # ------------------------------------------
#     vague_prompt = input("Step 1 → Enter a vague prompt (e.g., 'Tell me about technology'): ")
#     print(f"\nYour vague prompt: {vague_prompt}")

#     vague_response = generate_response(vague_prompt)
#     print("\nAI's response to the vague prompt:")
#     print("----------------------------------")
#     print(vague_response)

#     # ------------------------------------------
#     # STEP 2: Specific Prompt
#     # ------------------------------------------
#     specific_prompt = input("\nStep 2 → Make your prompt more specific "
#                             "(e.g., 'Explain how AI works in self-driving cars'): ")
#     print(f"\nYour specific prompt: {specific_prompt}")

#     specific_response = generate_response(specific_prompt)
#     print("\nAI's response to the specific prompt:")
#     print("--------------------------------------")
#     print(specific_response)

#     # ------------------------------------------
#     # STEP 3: Contextual Prompt
#     # ------------------------------------------
#     contextual_prompt = input("\nStep 3 → Add meaningful context "
#                               "(e.g., 'Given recent advancements, explain how AI makes real-time decisions in self-driving cars'): ")
#     print(f"\nYour contextual prompt: {contextual_prompt}")

#     contextual_response = generate_response(contextual_prompt)
#     print("\nAI's response to the contextual prompt:")
#     print("----------------------------------------")
#     print(contextual_response)

#     # ------------------------------------------
#     # Reflection Questions
#     # ------------------------------------------
#     print("\n==============================")
#     print(" Reflection Questions")
#     print("==============================")
#     print("1. How did the AI's response change when the prompt became specific?")
#     print("2. How did the AI's response improve with context added?")
#     print("3. Which prompt produced the best response? Why?\n")


# # Run tutorial
# silly_prompt()
























# import re
# from typing import List, Dict

# class PromptRefiner:
#     def __init__(self):
#         self.examples = [
#             {
#                 "vague": "Write about climate change",
#                 "refined": "Write a 300-word article for high school students explaining three main causes of climate change, using simple language and including real-world examples they can relate to.",
#                 "improvements": ["Added target audience", "Specified length", "Defined scope", "Clear tone"]
#             },
#             {
#                 "vague": "Create a function",
#                 "refined": "Create a Python function that validates email addresses using regex, returns True/False, and includes error handling for invalid input types.",
#                 "improvements": ["Specified language", "Clear purpose", "Defined output", "Added requirements"]
#             },
#             {
#                 "vague": "Analyze data",
#                 "refined": "Analyze this customer purchase data to identify buying patterns by age group. Calculate average order value per group, most popular product categories, and present findings in a comparison table.",
#                 "improvements": ["Specified data type", "Clear metrics", "Output format", "Actionable insights"]
#             }
#         ]

#     def analyze_prompt(self, prompt: str) -> Dict:
#         """Analyze a prompt and return issues, suggestions, and score"""
#         prompt_lower = prompt.lower().strip()
#         issues = []
#         suggestions = []

#         # Check length
#         if len(prompt) < 20:
#             issues.append("Prompt is too vague or short")
#             suggestions.append("Add more specific details about what you want")

#         # Check for audience
#         audience_keywords = ['for', 'audience', 'users', 'people', 'students', 'beginners', 'professionals']
#         if not any(keyword in prompt_lower for keyword in audience_keywords):
#             issues.append("No target audience specified")
#             suggestions.append("Specify who this is for (e.g., 'for beginners', 'for business owners')")

#         # Check for length/scope
#         if not re.search(r'\d+\s*(word|sentence|paragraph|page|line|item)', prompt_lower):
#             issues.append("No length or scope defined")
#             suggestions.append("Add length requirements (e.g., '500 words', '3 paragraphs')")

#         # Check for tone/style
#         style_keywords = ['tone', 'style', 'format', 'friendly', 'professional', 'casual', 'formal']
#         if not any(keyword in prompt_lower for keyword in style_keywords):
#             issues.append("No tone or style mentioned")
#             suggestions.append("Specify the tone (e.g., 'professional tone', 'casual style')")

#         # Check for specific requirements
#         requirement_keywords = ['include', 'with', 'containing', 'should have', 'must have', 'using']
#         if not any(keyword in prompt_lower for keyword in requirement_keywords):
#             issues.append("No specific requirements listed")
#             suggestions.append("List what should be included or specific methods to use")

#         # Calculate score
#         max_issues = 5
#         score = max(0, 100 - (len(issues) * 20))

#         return {
#             "issues": issues if issues else ["Good start! Your prompt has solid structure."],
#             "suggestions": suggestions,
#             "score": score
#         }

#     def display_examples(self):
#         """Display example prompts with refinements"""
#         print("\n" + "="*70)
#         print("EXAMPLE PROMPT REFINEMENTS")
#         print("="*70 + "\n")

#         for i, example in enumerate(self.examples, 1):
#             print(f"Example {i}:")
#             print(f"  ❌ VAGUE: \"{example['vague']}\"")
#             print(f"  ✅ REFINED: \"{example['refined']}\"")
#             print(f"  💡 Improvements: {', '.join(example['improvements'])}")
#             print()

#     def display_guide(self):
#         """Display prompt refinement guide"""
#         print("\n" + "="*70)
#         print("PROMPT REFINEMENT GUIDE")
#         print("="*70 + "\n")

#         print("KEY ELEMENTS TO INCLUDE:\n")
#         elements = [
#             ("Context", "Background information and purpose"),
#             ("Specificity", "Clear details and constraints"),
#             ("Audience", "Who is this for?"),
#             ("Length", "Word count or scope"),
#             ("Tone/Style", "How should it sound?"),
#             ("Format", "Desired output structure")
#         ]

#         for element, desc in elements:
#             print(f"  • {element:15} - {desc}")

#         print("\n\nREFINEMENT PROCESS:\n")
#         steps = [
#             "Start with your basic idea",
#             "Ask: Who is this for?",
#             "Define: What's the goal?",
#             "Specify: How long? What format?",
#             "Add: Tone, style, constraints",
#             "Review: Is it clear and actionable?"
#         ]

#         for i, step in enumerate(steps, 1):
#             print(f"  {i}. {step}")

#         print("\n" + "─"*70)
#         print("💡 PRO TIP: A good prompt answers: What? Who? How? What tone?")
#         print("─"*70 + "\n")

#     def run_interactive(self):
#         """Run interactive prompt refinement tool"""
#         print("\n" + "="*70)
#         print("AI PROMPT REFINEMENT TOOL")
#         print("="*70)
#         print("\nTransform vague prompts into clear, contextual instructions!\n")

#         while True:
#             print("\nOptions:")
#             print("  1. Test a prompt")
#             print("  2. View examples")
#             print("  3. View guide")
#             print("  4. Exit")

#             choice = input("\nEnter your choice (1-4): ").strip()

#             if choice == "1":
#                 print("\n" + "─"*70)
#                 prompt = input("Enter your prompt to analyze: ").strip()

#                 if not prompt:
#                     print("⚠️  Please enter a prompt!")
#                     continue

#                 print("\nAnalyzing prompt...\n")
#                 analysis = self.analyze_prompt(prompt)

#                 print("="*70)
#                 print(f"PROMPT QUALITY SCORE: {analysis['score']}%")
#                 print("="*70 + "\n")

#                 print("❌ ISSUES FOUND:")
#                 for issue in analysis['issues']:
#                     print(f"  • {issue}")

#                 if analysis['suggestions']:
#                     print("\n💡 SUGGESTIONS:")
#                     for suggestion in analysis['suggestions']:
#                         print(f"  • {suggestion}")

#                 print("\n" + "─"*70)

#             elif choice == "2":
#                 self.display_examples()

#             elif choice == "3":
#                 self.display_guide()

#             elif choice == "4":
#                 print("\n👋 Thanks for using the Prompt Refinement Tool!\n")
#                 break

#             else:
#                 print("⚠️  Invalid choice. Please enter 1-4.")


# def main():
#     """Main function to run the prompt refiner"""
#     refiner = PromptRefiner()
#     refiner.run_interactive()


# if __name__ == "__main__":
#     main()