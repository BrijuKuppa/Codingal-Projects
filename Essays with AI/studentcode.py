from google import genai
from google.genai import types
from colorama import init, Fore, Style, Back
from dotenv import load_dotenv
import os, time

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("api_key"))
except Exception as e:
    print(Fore.RED + Style.BRIGHT + f"\n\nThere was something wrong with the client. (Debug: {e})")
    exit()
def generate(prompt, temp=0.5): return client.models.generate_content(model = "gemini-3-flash-preview", contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])], config = types.GenerateContentConfig(temperature=temp)).text

init(autoreset=True)

def fancy_print(string, gap = 0.05, end: str = "\n", color = Fore.WHITE, style = Style.NORMAL, background = Back.BLACK):
    for i in string:
        print(color + style + background + i, flush=True, end="")
        time.sleep(gap)
    print(end)

def generate_essay():
    fancy_print("\n----Lets Generate your Essay!----\n", gap=0.087, color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX)

    fancy_print("How long is your essay? (Between 300 - 2000 characters.)", color=Fore.CYAN, style=Style.NORMAL, background=Back.LIGHTYELLOW_EX, end="")
    try: length = max(min(int(input("> ")), 2000), 300)
    except: length = 1000

    fancy_print("\nWhat is the topic of your essay?", color=Fore.YELLOW, style=Style.BRIGHT, background=Back.LIGHTMAGENTA_EX, end="")
    topic = input("> ")

    fancy_print("\nWhat type of essay are you writing? (e.g., Argumentative, Expository, Descriptive)", color=Fore.LIGHTCYAN_EX, style=Style.DIM, background=Back.LIGHTGREEN_EX, end="")
    variant = input("> ")

    fancy_print("\nWho is the target audience?", color=Fore.LIGHTGREEN_EX, style=Style.BRIGHT, background=Back.LIGHTYELLOW_EX, end="")
    target_audience = input("> ")

    fancy_print("\nAny specific points to include?", color=Fore.BLACK, style=Style.BRIGHT, background=Back.LIGHTMAGENTA_EX, end="")
    include = input("> ")

    fancy_print("\nWhat is your stance? (For/Against/Neutral)", color=Fore.LIGHTWHITE_EX, style=Style.BRIGHT, background=Back.LIGHTRED_EX, end="")
    stance = input("> ")

    fancy_print("\nAny references or sources?", color=Fore.BLACK, style=Style.NORMAL, background=Back.LIGHTCYAN_EX, end="")
    reference = input("> ")

    fancy_print("\nPreferred writing style? (Formal/Conversational/etc.)", color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTYELLOW_EX, end="")
    style = input("> ")

    fancy_print("\nDo you want an outline first?", color=Fore.WHITE, style=Style.BRIGHT, background=Back.LIGHTGREEN_EX, end="")
    outline = "Yes" if input("> ").lower() == 'yes' else "No"

    fancy_print("\nEnter temperature. (0.2 structured → 0.7 creative)", color=Fore.LIGHTYELLOW_EX, style=Style.BRIGHT, background=Back.LIGHTMAGENTA_EX, end="")
    try: temperature = max(min(float(input("> ")), 1), 0)
    except: temperature = 0.5

    fancy_print("\nBody style? (Step-by-step/Full draft):", color=Fore.BLACK, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX, end="")
    body = "step-by-step" if input("> ").lower() == 'step-by-step' else "full draft"


    fancy_print("\n\n----Output----", gap=0.087, color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX)
    print(generate(f"Write an essay with the info: length: {length} characters, topic: {topic}, type of essay: {variant}, target audience: {target_audience}, include these extra things: {include}, outline: {outline}, stance is: {stance}, reference is: {reference}, style: {style}, temperature: {temperature}, body of essay should be {body}."))


    # fancy_print("\n\n----Introduction----", gap=0.087, color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX)
    # print(generate(f"Write an introduction for a {variant} essay on {topic} with stance {stance}."))

    # fancy_print("\n\n----Body----", gap=0.087, color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX)
    # if body == "step-by-step": print(generate(f"Write a detailed {variant} essay about {topic} with stance {stance} in about {length} words."))
    # elif body == "full draft": print(generate(f"Write structured step-by-step arguments with evidence for an essay on {topic} with stance {stance}."))

    # fancy_print("\n\n----Connclusion----", gap=0.087, color=Fore.LIGHTMAGENTA_EX, style=Style.BRIGHT, background=Back.LIGHTCYAN_EX)
    # print(generate(f"Write a conclusion for a {variant} essay about {topic} with stance {stance}."))



    fancy_print("\n\nAny feedback?")
    input("> ")
    fancy_print("\nNoted.")

    fancy_print("\n\nBye!", color=Fore.RED)

if __name__ == "__main__":
    generate_essay()