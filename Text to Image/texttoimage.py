import requests
from io import BytesIO
from PIL import Image
import time
import random

HF_API_KEY = "hf_your_api_key"

def fancy_print(text, speed):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)

def generate(text):
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

    headers = {"Authorization" : HF_API_KEY}
    payload = {"inputs" : text}
    output = requests.post(url, headers=headers, json=payload)


    if output.status_code != 200:
        print(f"There was an unexpected error. {output} -- {output.status_code}")

    elif output.status_code == 200:
        return BytesIO(output.content)
    
def load():
    load_texts = [
    "Summoning pixels from the void...",
    "Convincing the AI that art is real...",
    "Teaching photons how to dance...",
    "Aligning imaginary brush strokes...",
    "Borrowing colors from another universe...",
    "Negotiating with the canvas...",
    "Letting creativity buffer...",
    "Rendering the unrenderable...",
    "Assembling atoms of imagination...",
    "Pretending to know what art means...",
    "Stretching the canvas...",
    "Mixing impossible paints...",
    "Spinning up extra creativity cores...",
    "Downloading inspiration...",
    "Painting outside the lines...",
    "Sharpening virtual pencils...",
    "Untangling artistic algorithms...",
    "Generating happy little accidents...",
    "Convincing pixels to cooperate...",
    "Making your imagination visible..."
    ]

    for i in range(5):
        fancy_print(random.choice(load_texts), 0.01)
        print("\n")
        time.sleep(0.5)    

def main():
    fancy_print("\n\nWelcome to Image Generator\n Describe your image to continue.", 0.01)

    text = input("\n> ")

    print("\n")
    load()

    image = generate(text)
    try:
        image.show()
    except:
        print(image)

    fancy_print("\nWould you like to save the generated image?", 0.01)

    print("\n")
    save = input("> ")

    if save == "yes" or save == "y":

        fancy_print("\nGive a name for your file.", 0.01)

        print("\n")
        name = input("> ")

        try:
            image.save(f"{name}.png")

        except:
            fancy_print("\nThere was an unexpected error.", 0.01)
    
    else:
        fancy_print("Exiting application...", 0.01)

if __name__ == "__main__":
    main()