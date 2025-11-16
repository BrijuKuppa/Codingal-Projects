import cv2
import numpy as np
from colorama import Fore, Style, init
from time import sleep
from PIL import Image
from io import BytesIO
import requests
import time

def mask_generator(image_name: str, precise: str = "non-sensitive"):
    image = cv2.imread(image_name)
    h, w = image.shape[:2]
    mask = np.zeros((h, w, 1), dtype=np.uint8)
    if precise == "sensitive":
        for x in range(h):
            for y in range(w):
                r, g, b = image[x, y]
                if r >= 210 and g >= 210 and b >= 210:
                    mask[x, y] = 1
                elif r < 230 and g < 230 and b < 230:
                    mask[x, y] = 0
    if precise == "non-sensitive":
        for x in range(h):
            for y in range(w):
                r, g, b = image[x, y]
                if r >= 230 and g >= 230 and b >= 230:
                    mask[x, y] = 1
                elif r < 250 and g < 250 and b < 250:
                    mask[x, y] = 0
    
    return mask

def fancy_print(text, time = 0.05, color = Fore.WHITE, style = Style.NORMAL):
    print(color + style + "", end="")
    for i in text:
        print(i, end="", flush=True)
        sleep(time)

def get_fixed(image, mask, prompt, api = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-inpainting", api_key = ""):
    header = {"Authorization" : f"Bearer {api_key}"}
    payload = {"prompt" : prompt}
    with open(image, "rb") as b:
        image_data = b.read()
    success, mask_data = cv2.imencode(".png", mask)

    files = {
        "image" : ("image.png", image_data, "image/png"),
        "mask" : ("mask.png", mask_data, "image/png")
    }
    
    try:
        result = requests.post(api, headers=header, data=payload, files=files)
        Image.open(BytesIO(result.content))
    except Exception as e:
        fancy_print(f"\nThere was an unexpected error. Please contact the developer and rerun the program. (Debug: '{e}')")

def main():
    fancy_print("\n\nLoading 'Image Fixer'  ", color = Fore.LIGHTYELLOW_EX, style = Style.BRIGHT)
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    for i in range(100):
        frame = frames[i % len(frames)]
        print(f"\rLoading 'Image Fixer' {frame}", end="")
        time.sleep(0.09)
    fancy_print("\nLoaded!", color = Fore.GREEN, style = Style.BRIGHT)
    fancy_print("\n\nDisclaimer:\nThis tool attempts to enhance the images you upload. \nResults may vary, and perfect improvement is not guaranteed. \nYou are responsible for the content you provide.", color=Fore.LIGHTRED_EX, style=Style.BRIGHT)

    while True:
        fancy_print("\n\nChoose an option to continue:\n 1. See an example\n 2. Try it out\n 3. Exit\n", color = Fore.CYAN)
        choice = input("").lower().strip()

        if choice in ("1", "see an example"):
            mask = mask_generator(r"C:\Users\briju\OneDrive\Pictures\Screenshots\Screenshot 2025-11-09 142358.png")
            get_fixed(r"C:\Users\briju\OneDrive\Pictures\Screenshots\Screenshot 2025-11-09 142358.png", mask, "Please fix as if image was never damaged.")
        elif choice in ("2", "try it out"):
            fancy_print("\n\nEnter an image path for us to use.\n", color=Fore.LIGHTGREEN_EX)
            path = input("")
            fancy_print("\nTo generate a mask for your image, please choose between sensitive or non-senstive white detection.\n", color=Fore.LIGHTGREEN_EX)
            choice = input("")
            fancy_print("\nPlease type any other specifications when we generate our image.\n", color=Fore.LIGHTGREEN_EX)
            prompt = input("")
            try:
                fancy_print("\n\nGenerating mask ", color = Fore.LIGHTYELLOW_EX, style = Style.BRIGHT)
                for i in range(50):
                    frame = frames[i % len(frames)]
                    print(f"\rGenerating mask {frame}", end="")
                    time.sleep(0.09)
                fancy_print("\n\nLoading image ", color = Fore.LIGHTYELLOW_EX, style = Style.BRIGHT)
                for i in range(50):
                    frame = frames[i % len(frames)]
                    print(f"\rLoading image {frame}", end="")
                    time.sleep(0.09)

                mask = mask_generator(path, precise=choice, )
                get_fixed(path, mask, prompt=prompt)
            except Exception as e:
                fancy_print(f"\nThere was an unexpected error. Please contact the developer and rerun the program. (Debug: '{e}')")

        elif choice in ("3", "exit"):
            fancy_print("\n\nExiting   ", color=Fore.RED, style=Style.BRIGHT)
            for i in range(100):
                frame = frames[i % len(frames)]
                print(f"\rExiting {frame}", end="")
                time.sleep(0.09)
            exit()
        else:
            fancy_print("\n\nPut a valid answer.\n", color=Fore.RED, style=Style.BRIGHT)

if __name__ == "__main__":
    main()