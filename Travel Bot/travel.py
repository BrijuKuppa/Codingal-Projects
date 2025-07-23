import colorama
from colorama import Fore, Style
import re, random

colorama.init(autoreset=True)

destinations = {
    "beaches": ["Maldives", "Bora Bora", "Hawaii", "Bahamas"],
    "mountains": ["Himalayas", "Rocky Mountains", "Andes", "Alps"],
    "cities": ["New York", "Tokyo", "Paris", "London"],
}

jokes = [
    "How can you tell elephants love to travel? They always pack their own trunk!",
    "Why did the witch stay in a hotel? She heard they had great broom service!",
    "Where do sharks go on vacation? Finland!",
    "Where do sheep go on vacation? The Baaa-hamas!",
    "Where do hamsters go on vacation? Hamsterdam!",
    "What do frogs like to drink on a hot summer's day? Croak-a-Cola!",
    "How do rabbits get to their holiday destination? By hare-plane!",
    "What did the pig say on the beach? I'm bacon!"
    "What travels around the world but stays in one corner? A stamp!"
    "What do you get when you cross an airplane with a magician? A flying sorcerer!"
]

tips1 = [
    " - Plan It Out.",
    " - Choose the Right Luggage and Know Your Airline's Baggage Policy.",
    " - Carry Essentials + One Outfit in Your Carry-On Bag.",
]

tips2 = [
    " - Coordinate Your Outfits for Maximum Versatility.",
    " - Layering Is Key.",
    " - Opt for Wrinkle-Proof Fabrics."
]

tips3 = [
    " - Use Packing Cubes and Roll Your Clothes.",
    " - Pack Versatile Shoes That Match Multiple Outfits.",
    " - Wear Your Bulkiest Items in Transit."  
]


def normalize(s):
    return re.sub("/s+", "", s).lower().strip()


def recommend():
    preference = input(f"{Fore.MAGENTA}\nWhere would you like to travel to? ")

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"{Fore.BLUE}{preference.title()}, what a great option!\nLet me give a suggestion.\n {suggestion}\nWhat do you think 😀?")
        
        choice = input("(type 'yes' or 'no') ")

        if choice == "yes":
            print(f"{Fore.GREEN}That is great! Safe travels!")
            help()
        elif choice == "no":
            print(f"{Fore.RED}Sorry to hear that 🫤! Do you want me to suggest another location?")
            choice2 = input("(type 'yes' or 'no') ")
            if choice2 == "yes":
                print(f"{Fore.YELLOW}Okay! Lets try this again.")
                recommend()
            elif choice2 == "no":
                print(f"{Fore.LIGHTRED_EX}Okay then 😅! Returning to menu...")
                help()
            else:
                print(f"{Fore.YELLOW}I didn't seem to understand. Returning to help menu...")
                help()
        else:
            print(f"{Fore.YELLOW}I didn't seem to understand. Returning to help menu...")
            help()
    
    else:
        print(f"{Fore.YELLOW}I didn't seem to understand your answer. Either you misspelled, or your destination wasn't in my database. Please try again.")
        recommend()


def packing():
    print(f"{Fore.BLUE}\nOkay, but first, before I tell you some tips, I need some info. Answer the questions below:\n")

    days = normalize(input("How many days are you going? "))
    location = normalize(input("Where are you going? "))

    print(f"{Fore.CYAN}Thank you for answering the questions! Here are some packing tips for {days} days in {location.title()}:\n")
    print(f"{Fore.GREEN}{random.choice(tips1)}")
    print(f"{Fore.GREEN}{random.choice(tips2)}")
    print(f"{Fore.GREEN}{random.choice(tips3)}")
    help()


def joke():
    print(f"{Fore.LIGHTMAGENTA_EX}\nWant to hear a joke? Here is a good one:\n")
    print(f"{random.choice(jokes)}")
    help()


def help():
    print(f"{Fore.LIGHTCYAN_EX}\nOptions:\n - type 'recommend' to recommend a location to travel to.\n - type 'pack' to recommend packing tips\n - type 'jokes' to hear a joke.\n - type 'exit' to leave the application.'")

print(f"\n{Fore.LIGHTGREEN_EX}Hello 👋! I'm TravelBot©. How can I help you today?")
help()

while True:

    user_input = normalize(input("\nType here: "))

    if user_input == "pack":
        packing()
        continue

    elif user_input == "jokes":
        joke()
        continue

    elif user_input == "recommend":
        recommend()
        continue

    elif user_input == "exit":
        print(f"{Fore.RED}It was nice talking to you. Safe travels!")
        break   

    else:
        print(f"{Fore.RED}I didn't undertsand your answer. Please try again.")
        continue