print("Hello, I am a chatbot.")
print("What is your name?")

name = input("Put your name here:")
print(f"Hello, {name}. Can you also say how old are you?")

age = input("Put your age here:")
print(f"It is cool that you are {age} years old.")

print("Can you also tell me, how are you feeling today?")
feeling = input("Put your feeling here (good/bad):").lower()

if feeling == "good":
    print("I'm glad that you are feeling good today!")

elif feeling == "bad":
    print("I'm sorry to hear that you are not feeling good today.")

else:
    print("That is not a valid answer.")

print(f"It was nice to meet you, {name}.")
print("Goodbye!")