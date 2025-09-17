from config import HF_API_KEY
from colorama import Fore, Style, init
import requests
import time

init(autoreset=True)

def summerize(model: str, text: str, min: int, max: int):
    url = model
    
    headers = {"Authorization" : HF_API_KEY}
    payload = {"inputs" : text,  "min_length" : min, "max_length" : max}

    for i in range(5):
        output = requests.post(model, headers=headers, json=payload)
        if output.status_code == 200:
            return output.json
        
        elif output.status_code == 503:
            print(Fore.YELLOW + "There was a problem. Please wait as we try to fix the problem...")
            time.sleep(5)
        
        else:
            print(Fore.RED + Style.BRIGHT + f"There was a problem with the API. {output.status_code} -- {output.text}")
            break


def main():
    print(Fore.GREEN + "\nRunning 'Summerization Code' ...\n\n")

    while True:
        print(Fore.CYAN + "\nTo start, enter in a model, or press enter to use the default one.")
        model = input(Fore.LIGHTRED_EX + "> ")

        print(Fore.CYAN + "\nTo continue, type in the text you want to summerize.")
        text = input(Fore.LIGHTRED_EX + "> ")

        print(Fore.GREEN + "\nFor the model to summerize, choose from these options:\n Short\n Accurate\n Custom")
        size = input(Fore.LIGHTRED_EX + "> ").lower().strip()
        if size == "short":
            min_length, max_length = 20, 100
        elif size == "accurate":
            min_length, max_length = 30, 200
        elif size == "custom":
            try:
                print(Fore.YELLOW + "\nType a minimum length:")
                min_length = int(input(Fore.LIGHTRED_EX + "> "))
            except:
                print(Fore.RED + Style.BRIGHT + f"Your input was not understood. We are restarting the program...")
                continue
            
            try:
                print(Fore.YELLOW + "\nType a maximum length:")
                max_length = int(input(Fore.LIGHTRED_EX + "> "))
            except:
                print(Fore.RED + Style.BRIGHT + f"Your input was not understood. We are restarting the program...")
                continue

        else:
            print(Fore.RED + Style.BRIGHT + f"Your input was not understood. We are restarting the program...")
            continue

        print(Fore.GREEN + "\nResults:")
        if model == "":
            results = summerize(f"https://api-inference.huggingface.co/models/google/pegasus-xsum", text, min_length, max_length)
            print(results)
        else:
            results = summerize(f"https://api-inference.huggingface.co/models/{model}", text, min_length, max_length)
            print(results)

if __name__ == "__main__":
    main()