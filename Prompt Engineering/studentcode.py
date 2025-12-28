from google import genai

api_key = input("\nEnter your Genai API key. ")

client = genai.Client(api_key=api_key)
def generate(prompt):
    try:
        return client.models.generate_content(model="gemini-2.0-flash", contents=prompt).text
    except Exception as e:
        return f"\nOh noes! Mistakes happen, just like in code. Maybe an API error? (Debug: {e})"

def main():
    print("\nLets start Prompt Engineering!\n\nChoose an activity, we reccomend you go in order! (number):\n 1. What is prompt engineering?\n 2. Vague Prompts\n 3. Specific Prompt\n 4. Contextual Prompt\n 5. Reflection\n 6. Exit\n\n")

    while True:
        choice = input("> ").lower()

        if choice == "1" or choice == "one":
            print("\nPrompt engineering is the practice of carefully crafting the instructions you give to an AI so it produces accurate, useful, and relevant responses. Since AI doesn't “think” like a human, the way you phrase your prompt has a big impact on the quality of its answer. By being specific, providing context, setting constraints like length or style, and sometimes assigning the AI a role (like “act as a teacher”), you can guide it to give exactly what you want. Essentially, prompt engineering is about learning how to communicate effectively with AI to get the best results.")
        elif choice == 2 or choice == "two":
            print("\nEnter a broad/vague prompt. (e.g., Tell me about the ocean.)")
            vague_prompt = input("> ")
            print(f"\nResult: {generate(vague_prompt)}")
        elif choice == 3 or choice == "three":
            print("\nEnter a precise/specifc prompt. (e.g., Tell me about what seahorses eat when they are hungry.)")
            vague_prompt = input("> ")
            print(f"\nResult: {generate(vague_prompt)}")
        elif choice == 4 or choice == "four":
            print("\nEnter a prompt with context. (e.g., Explain interesting facts about seahorses, including their habitat, features, and unique reproduction, in a way a middle school student can understand.)")
            vague_prompt = input("> ")
            print(f"\nResult: {generate(vague_prompt)}")
        elif choice == 5 or choice == "five":
            print("\nThink about these questions in your head:\n 1. How did the AI's response change when the prompt was made more specific?\n 2. How did the AI's response improve with the added context?\n 3. Which version of the prompt gave the best response? Why?\n")
        elif choice == 6 or choice == "exit" or choice == "six":
            exit()
        else:
            print("\nEnter an actual choice.")

if __name__ == "__main__":
    main()