import requests
from config import HF_API_KEY
import re
import time
import os

def sentement_analysis(text):
    url_sent = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    print(requests.get(url_sent))
    split = re.split(r"(?<=[?!.])\s+", text)
    headers = {"Authorization" : f"Bearer {HF_API_KEY}"}
    
    for i, sen in enumerate(split, 1):
        payload = {"inputs" : sen}
        output = requests.post(url_sent, headers=headers, json=payload)
        if output.status_code != 200:
            print(f"There was an unexpected error. {output.status_code}")
        return output.json()

def translation(text):
    url_transla = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-de"
    split = re.split(r"(?<=[?!.])\s+", text)
    headers = {"Authorization" : f"Bearer {HF_API_KEY}"}
    
    for i, sen in enumerate(split, 1):
        payload = {"inputs" : sen}
        output = requests.post(url_transla, headers=headers, json=payload)
        if output.status_code != 200:
            fancy_print(f"There was an unexpected error. {output.status_code}", 0.1)
            return
        return output.json()[0]['translation_text']

def fancy_print(string, speed):
    string = string
    for i in string:
        print(i, end="", flush=True)
        time.sleep(speed)

def main():
    fancy_print("\nRunning 'Text Analysis App'", 0.05)
    fancy_print("....", 1)

    fancy_print("\n\n--------------", 0.01)
    fancy_print("\nChoice an option to get started.\n Sentiment\n Translation", 0.01)
    choice = input("\n> ").strip().lower()
    fancy_print("--------------\n", 0.01)

    if choice == "sentiment":
        while True:
            fancy_print("\n\n--------------", 0.01)
            fancy_print("\nChoice an option to continue.\n File Analysis\n User Input \n Exit", 0.01)
            choice = input("\n> ").strip().lower()
            fancy_print("--------------\n", 0.01)

            if choice == "file analysis" or choice == "fileanalysis":
                while True:
                    text = os.listdir("analysisFiles")
                    print("\n\n", text)
                    fancy_print("\n\n--------------", 0.01)
                    fancy_print("\nThe options are shown above. Please type your choice exactly how it is shown to contiue.", 0.01)
                    choice = input("\n> ")
                    fancy_print("--------------\n", 0.01)

                    if choice in text:
                        fancy_print("\n\n--------------", 0.01)
                        fancy_print("\nChoose an option to contiue.\n Read\n Write\n New\n Delete\n Back", 0.01)
                        choice_type = input("\n> ").lower().strip()
                        fancy_print("--------------\n", 0.01)
                        file_path = os.path.join("analysisFiles", choice)

                        if choice_type == "read":
                            fancy_print("\n\n--------------\n", 0.01)
                            with open(file_path, "r") as file:
                                text = file.read()
                                print(text)
                            split = re.split(r"(?<=[?!.])\s+", text)
                            for i in split:
                                print(sentement_analysis(i))
                            fancy_print("--------------\n", 0.01)
                        elif choice_type == "write":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nChoose an option to contiue.\n Overwrite\n Append", 0.01)
                            choice_action = input("\n> ").lower().strip()
                            fancy_print("--------------\n", 0.01)
                            
                            if choice_action == "overwrite":
                                with open(file_path, "w") as file:
                                    fancy_print("\n\n--------------", 0.01)
                                    fancy_print("\nType below.", 0.01)
                                    choice_action = input("\n> ").lower().strip()
                                    file.write(choice_action)
                                    fancy_print(f"\n{choice} has been overwritten.\n", 0.01)
                                    fancy_print("--------------\n", 0.01)
                            elif choice_action == "append":
                                with open(file_path, "a") as file:
                                    fancy_print("\n\n--------------", 0.01)
                                    fancy_print("\nType below.", 0.01)
                                    choice_action = input("\n> ").lower().strip()
                                    file.write(" " + choice_action)
                                    fancy_print(f"\n{choice} has been appended.\n", 0.01)
                                    fancy_print("--------------\n", 0.01)
                            else:
                                fancy_print("Your input was invalid. Please try again.", 0.01)
                        elif choice_type == "delete":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nWe are going to delete the file you had chose. Do you wish to continue?", 0.01)
                            choice_yn = input("\n> ").lower().strip()
                            fancy_print("--------------\n", 0.01)

                            if choice_yn == "yes" or choice_yn == "y":
                                fancy_print("\n\n--------------", 0.01)
                                os.remove(file_path)
                                fancy_print("\nYour file as been deleted.\n", 0.01)
                                fancy_print("--------------\n", 0.01)
                            else:
                                fancy_print("\n\n--------------", 0.01)
                                fancy_print("\nYour file has not been changed.\n", 0.01)
                                fancy_print("--------------\n", 0.01)
                        elif choice_type == "new":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nType a new name to continue. Make sure you put the file type in your name. (The reccomended file type is '.txt')", 0.01)
                            choice_name = input("\n> ").strip()
                            fancy_print("--------------\n", 0.01)

                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nType to continue.", 0.01)
                            choice_contents = input("\n> ").strip()
                            fancy_print("--------------\n", 0.01)

                            fancy_print("\n\n--------------", 0.01)
                            new_path = os.path.join("analysisFiles", choice_name)
                            try:
                                with open(new_path, "x") as file:
                                    file.write(choice_contents)
                            except:
                                fancy_print("\nThere was an unexpected error.\n", 0.01)
                                continue
                            fancy_print("\nYour new file as been saved.\n", 0.01)
                            fancy_print("--------------\n", 0.01)
                        elif choice_type == "back":
                            break
                        else:
                            fancy_print("Your input was invalid. Please try again.", 0.01)
                    else:
                        fancy_print("Your input was invalid. Please try again.", 0.01)
            elif choice == "user input" or choice == "userinput":
                fancy_print("\n\n--------------", 0.01)
                fancy_print("\nType your input to continue.", 0.01)
                choice = input("\n> ")
                fancy_print("--------------\n", 0.01)
                
                fancy_print("\n\n--------------\n", 0.01)
                split = re.split(r"(?<=[?!.])\s+", choice)
                for i in split:
                    print(translation(i))
                fancy_print("--------------\n", 0.01)
            elif choice == "exit":
                fancy_print("\nExiting 'Text Analysis App'", 0.05)
                fancy_print("....", 1)
                exit()
            else: 
                fancy_print("Your input was not understood. Lets try again.\n\n", 0.01)
                continue

    elif choice == "translation":
        while True:
            fancy_print("\n\n--------------", 0.01)
            fancy_print("\nChoice an option to continue.\n File Analysis\n User Input", 0.01)
            choice = input("\n> ").strip().lower()
            fancy_print("--------------\n", 0.01)

            if choice == "file analysis" or choice == "fileanalysis":
                while True:
                    text = os.listdir("analysisFiles")
                    print("\n\n", text)
                    fancy_print("\n\n--------------", 0.01)
                    fancy_print("\nThe options are shown above. Please type your choice exactly how it is shown to contiue.", 0.01)
                    choice = input("\n> ")
                    fancy_print("--------------\n", 0.01)

                    if choice in text:
                        fancy_print("\n\n--------------", 0.01)
                        fancy_print("\nChoose an option to contiue.\n Read\n Write\n New\n Delete\n Back", 0.01)
                        choice_type = input("\n> ")
                        fancy_print("--------------\n", 0.01)
                        file_path = os.path.join("analysisFiles", choice)

                        if choice_type == "read":
                            fancy_print("\n\n--------------\n", 0.01)
                            with open(file_path, "r") as file:
                                text = file.read()
                                print(text)
                            split = re.split(r"(?<=[?!.])\s+", text)
                            for i in split:
                                print(translation(i))
                            fancy_print("--------------\n", 0.01)
                        elif choice_type == "write":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nChoose an option to contiue.\n Overwrite\n Append", 0.01)
                            choice_action = input("\n> ").lower().strip()
                            fancy_print("--------------\n", 0.01)
                            
                            if choice_action == "overwrite":
                                with open(file_path, "w") as file:
                                    fancy_print("\n\n--------------", 0.01)
                                    fancy_print("\nType below.", 0.01)
                                    choice_action = input("\n> ").lower().strip()
                                    file.write(choice_action)
                                    fancy_print(f"\n{choice} has been overwritten.", 0.01)
                                    fancy_print("--------------\n", 0.01)
                            elif choice_action == "append":
                                with open(file_path, "a") as file:
                                    fancy_print("\n\n--------------", 0.01)
                                    fancy_print("\nType below.", 0.01)
                                    choice_action = input("\n> ").lower().strip()
                                    file.write(" " + choice_action)
                                    fancy_print(f"\n{choice} has been appended.\n", 0.01)
                                    fancy_print("--------------\n", 0.01)
                            else:
                                fancy_print("Your input was invalid. Please try again.", 0.01)
                        elif choice_type == "delete":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nWe are going to delete the file you had chose. Do you wish to continue?", 0.01)
                            choice_yn = input("\n> ").lower().strip()
                            fancy_print("--------------\n", 0.01)

                            if choice_yn == "yes" or choice_yn == "y":
                                fancy_print("\n\n--------------", 0.01)
                                os.remove(file_path)
                                fancy_print("\nYour file as been deleted.\n", 0.01)
                                fancy_print("--------------\n", 0.01)
                            else:
                                fancy_print("\n\n--------------", 0.01)
                                fancy_print("\nYour file has not been changed.\n", 0.01)
                                fancy_print("--------------\n", 0.01)
                        elif choice == "new":
                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nType a new name to continue. Make sure you put the file type in your name. (The reccomended file type is '.txt')", 0.01)
                            choice_name = input("\n> ").strip()
                            fancy_print("--------------\n", 0.01)

                            fancy_print("\n\n--------------", 0.01)
                            fancy_print("\nType to continue.", 0.01)
                            choice_contents = input("\n> ").strip()
                            fancy_print("--------------\n", 0.01)

                            fancy_print("\n\n--------------", 0.01)
                            new_path = os.path.join("analysisFiles", choice_name)
                            try:
                                with open(new_path, "x") as file:
                                    file.write(choice_contents)
                            except:
                                fancy_print("\nThere was an unexpected error.\n", 0.01)
                                continue
                            fancy_print("\nYour new file as been saved.\n", 0.01)
                            fancy_print("--------------\n", 0.01)
                        elif choice_type == "back":
                            break
                        else:
                            fancy_print("Your input was invalid. Please try again.", 0.01)
                    else:
                        fancy_print("Your input was invalid. Please try again.", 0.01)
            elif choice == "user input" or choice == "userinput":
                fancy_print("\n\n--------------", 0.01)
                fancy_print("\nType your input to continue.", 0.01)
                choice = input("\n> ")
                fancy_print("--------------\n", 0.01)
                
                fancy_print("\n\n--------------\n", 0.01)
                split = re.split(r"(?<=[?!.])\s+", choice)
                for i in split:
                    print(translation(i))
                fancy_print("--------------\n", 0.01)
            elif choice == "exit":
                fancy_print("\nExiting 'Text Analysis App'", 0.05)
                fancy_print("....", 1)
                exit()
            else: 
                fancy_print("Your input was not understood. Lets try again.\n\n", 0.01)
                continue

    else:
        fancy_print("Your input was not understood. Lets restart the program.\n\n", 0.01)
        main()

if __name__ == "__main__":
    main()