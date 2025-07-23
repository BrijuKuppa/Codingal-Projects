import colorama
from colorama import Fore, Style
from textblob import TextBlob
from texttable import Texttable

colorama.init()

print(f"\n{Fore.CYAN}Welcome to the Sentiment Analysis Tool 👋! {Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA} First, what is your name? {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "User"

conversation_history = []

print(f"{Fore.CYAN}Hello, {user_name}! Can you write about how you feel today? {Style.RESET_ALL}\n")
print(f"{Fore.YELLOW}Options:\n'reset' - restart conversation\n'history' - view what you have written\n'leave' - exit the program{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.LIGHTCYAN_EX}\nWrite your thoughts and imagination... {Style.RESET_ALL}").lower().strip()

    if user_input == "leave":
        print(f"{Fore.RED}Exiting application...\nGoodbye!{Style.RESET_ALL}")
        break

    elif user_input == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}\nAw Snap 💥! It seems you don't have any conversation history, keep writing!")
            continue
        else:
            print(f"{Fore.GREEN}\nHere is what we talked about so far:{Style.RESET_ALL}")
            table = Texttable()
            table.add_row(["ID", "Text", "Polarity", "Sentiment"])
            for i, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                table.add_row([i, color+text+Style.RESET_ALL, f"{polarity:.2f}", sentiment_type + " " + emoji])
            print(table.draw())
            continue

    elif user_input == "reset":
        print(f"{Fore.YELLOW}\nAre you sure you want to {Fore.RED}delete{Fore.YELLOW} your conversation history?{Style.RESET_ALL}")
        sure = input(f"{Fore.RED}Type 'yes' to confirm, and 'no' to abort. {Style.RESET_ALL}").lower()
        if sure == "yes":
            conversation_history = []
            print(f"{Fore.LIGHTGREEN_EX}\nI have wiped our conversation. Let's start fresh ✨!{Style.RESET_ALL}")
        
        elif sure == "no":
            print(f"{Fore.YELLOW}\nAction aborted. Lets keep talking 😊!{Style.RESET_ALL}")
            continue
        else:
            print(f"{Fore.YELLOW}\nInvalid, Action aborted. Lets keep talking 😊!{Style.RESET_ALL}")
            continue

    else:
        polarity = TextBlob(user_input).sentiment.polarity

        if polarity > 0:
            sentiment_type = "Positive"
            color = Fore.GREEN
            emoji = "😊"
        elif polarity < 0:
            sentiment_type = "Negative"
            color = Fore.RED
            emoji = "😞"
        else:
            sentiment_type = "Neutral"
            color = Fore.YELLOW
            emoji = "😐"

        conversation_history.append((user_input, polarity, sentiment_type))
        print(f"{color}Bases on your writing, I sense that you are feeling {sentiment_type}, {emoji}, with a polarity of {polarity:.2f}.\n{Style.RESET_ALL}")

        
