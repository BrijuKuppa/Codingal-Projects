import requests
import time

def fancy_print(string):
    print("\n")
    string = string
    for i in string:
        print(i, end="", flush=True)
        time.sleep(0.01)

def main():
    topic = None
    fancy_print("-----------------------------\nWelcome to your API Encyclopedia!\nTo get started, chose a proper category.\n-----------------------------")
    choice = input("\n\n>").lower().strip()
    filtered_choice = choice.replace(" ", "")
    topic = filtered_choice

    try:
        fancy_print("-----------------------------\nNow that you have chose your category,\nPress enter to see the facts related to your category!\nOr, type 'day' to see the fact of the day, and type 'q' to exit.\n-----------------------------")
        while True:
            url = f"https://uselessfacts.jsph.pl/api/v2/facts/random?language=en&category={topic}"
            facts = requests.get(url)
            parse = facts.json()

            option = input("\n\n\n>")
            if option == "":
                fancy_print(parse["text"])
            elif option == "day":
                url = f"https://uselessfacts.jsph.pl/api/v2/facts/today?language=en&category={topic}"
                facts = requests.get(url)
                parse = facts.json()
                fancy_print(parse["text"])
            elif option == "q":
                fancy_print("It is a proven fact that you need to go now. Bye!\n-----------------------------\n\n")
                exit()
            else:
                fancy_print("You option is not recognizable. Please try again.")

    except Exception as e:
        fancy_print("There was an unexpected error. Please try again.")
        print(e)

if __name__ == "__main__":
    main()