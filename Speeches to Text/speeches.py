import os
import wave
import speech_recognition
from datetime import datetime
from time import sleep
import colorama
from colorama import Fore, Style

colorama.init()

def fancy_print(text, time = 0.05, color = Fore.WHITE, style = Style.NORMAL):
    print(color + style + "", end="")
    for i in text:
        print(i, end="", flush=True)
        sleep(time)

def read_files(foldername: str):
    files = os.listdir(foldername)

    for i in files:
        filename = f"{foldername}/"+i
        with wave.open(filename, "rb") as r:
            width = r.getsampwidth()
            frames = r.readframes(r.getnframes())
            rate = r.getframerate()
            sr = speech_recognition.Recognizer()
            audio = speech_recognition.AudioData(frames, rate, width)
        try:
            text = sr.recognize_google(audio)
            fancy_print(f"\n\nResult for {i}:\n {text}", color=Fore.GREEN, style=Style.BRIGHT)
        except BaseException as e:
            fancy_print(f"\nThere was an unexpected error. (Debug: {e})", color=Fore.RED, style=Style.BRIGHT)

def main():
    fancy_print("\n\nWelcome, User!", color=Fore.CYAN)
    fancy_print("\nTo start, please make sure you have uploaded a folder of '.wav' files.", color=Fore.CYAN)

    stuff = [i for i in os.listdir(r"C:\Brijesh_ProjectFolder\Codingal_Projects\Speeches to Text") if os.path.isdir(i)]
    if stuff != []:
        while True:
            fancy_print("\n\nHere is what we have found:", color=Fore.GREEN)
            for i, n in enumerate(stuff, 1): fancy_print(f"\n {i}. {n}", color=Fore.BLUE)
            fancy_print("\n\nChoose your folder (number) to scan. ")
            path = int(input("")) - 1
            try:
                fancy_print("\nScanning files.....", time=0.1, color=Fore.YELLOW)
                read_files(stuff[path])
            except Exception as e:
                fancy_print(f"\nThere was an unexpected error. (Debug: {e})", color=Fore.RED, style=Style.BRIGHT)

            fancy_print("\n\nDo you want to continue the program? ", color=Fore.YELLOW)
            go = input("") 
            if go == "yes": fancy_print("\n\nChoose a folder of '.wav' files.", color=Fore.CYAN)
            else: fancy_print("\n\nGoodbye!", color=Fore.BLACK); break
    else:
        fancy_print("We have detected no folders. Please put a folder of sound files in the folder this program is in, and rerun the code.", color=Fore.RED, style=Style.BRIGHT)


if __name__ == "__main__":
    main()