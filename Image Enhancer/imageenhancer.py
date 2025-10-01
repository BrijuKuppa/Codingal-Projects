import requests
from io import BytesIO
from PIL import Image, ImageShow
import cv2
import numpy as np
import time
from waiting import wait

HF_API_KEY = "yourapikey"


def fancy_print(text: str, speed=0.01):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)


def generate(text):
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    fancy_print("\nType any specifications for the generator to avoid when making the image.", 0.01)
    negative_prompt = input("\n> ")
    fancy_print("\nPlease wait as we communicate to the API...\n", 0.01)
    headers = {"Authorization" : f"Bearer {HF_API_KEY}"}
    if negative_prompt == "":
        payload = {"inputs" : text}
    else:
        payload = {"inputs" : text, 
                   "options": {
                       "negative_prompt" : negative_prompt,
                       "guidance_scale" : 7.5
                   }}
    output = requests.post(url, headers=headers, json=payload)


    if output.status_code != 200:
        print(f"❌ There was an unexpected error. {output} -- {output.status_code}")

    elif output.status_code == 200:
        return BytesIO(output.content), BytesIO(output.content).getvalue()

    

def enhancer(buffer_image, option=""):
    array = np.frombuffer(buffer_image, dtype=np.uint8) # Decode the image from a buffer (bytes) to a readable format for cv2
    image = cv2.imdecode(array, cv2.IMREAD_COLOR)
    shape = image.shape

    if image.any():
        cv2.putText(image, "AI Generated", (shape[0] - 300, shape[1] - 100), cv2.FONT_HERSHEY_COMPLEX, 1, (200, 200, 200))

        if option == "":
            cv2.imshow("Image", image)
            cv2.waitKey()
            return image
        elif option == "illuminate":
            more_contrast = cv2.convertScaleAbs(image, alpha=1.1, beta=50)
            final = cv2.GaussianBlur(more_contrast, (5, 5), 30)
            cv2.imshow("Illuminated Image", final)
            cv2.waitKey()
            return final
        elif option == "nocturnal":
            more_contrast = cv2.convertScaleAbs(image, alpha=1.4, beta=50)
            final = cv2.GaussianBlur(more_contrast, (3, 3), 10)
            cv2.imshow("Illuminated Image", final)
            cv2.waitKey()
            return final
            

def main():
    fancy_print("\n\n🔃 Loading Image Enhancer...\n✅ Loaded!\n", 0.1)
    fancy_print("\nDescribe your image to continue.")
    text = input("\n> ")

    bytesio, buffer = generate(text)

    try:
        image = Image.open(bytesio)
        image.show()
        fancy_print("\n✨ Your generated image should have shown up on your screen.\n")
    except:
        fancy_print("\n❌ There was an unexpected error.")
        fancy_print("\n🔃 Please restart the program.")
        exit()

    fancy_print("\nWould you like to add any enhancements?")
    enhance = input("\n> ")

    if enhance == "yes":
        options = ["illuminate", "nocturnal"]
        fancy_print("\nChoose from a set amount of options:\n Illuminate\n Nocturnal")
        
        enhancements = input("\n> ").strip().lower()
        if enhancements in options:
            fancy_print("\nPlease wait as we enhance your image...\n", 0.1)
            fancy_print("Your final image will be shown. Please close it to continue.\n")
            image = enhancer(buffer, option=enhancements)
        else:
            fancy_print("\nYour image will stay the same.\n")
            fancy_print("Your final image will be shown. Please close it to continue.\n")
            image = enhancer(buffer)
                
    else:
        fancy_print("\nYour image will stay the same.\n")
        fancy_print("Please wait as we make the finishing touches...\n", 0.2)
        fancy_print("Your final image will be shown. Please close it to continue.\n")
        image = enhancer(buffer)
    fancy_print("\nWould you like to save the generated image?")
    save = input("\n> ")

    if save == "yes" or save == "y":
        fancy_print("\nGive a name for your file.")
        name = input("\n> ")

        try:
            fancy_print("\n💾 Saving your image...", 0.1)
            cv2.imwrite(f"{name}.png", image)
            fancy_print("\n✅ Saved succesfully!", 0.1)
        except:
            fancy_print("\n❌ There was an unexpected error.")
            fancy_print("\nYour image was not saved.")
    else:
        fancy_print("\nYour image was not saved.")

    fancy_print("\n\n╰┈➤  Exiting application...")


if __name__ == "__main__":
    main()

    # img = np.zeros((1000, 1000, 3), dtype=np.uint8)
    # img[:] = (255, 0, 0)  # BGR -> blue

    # # Encode to PNG (bytes)
    # _, encoded_img = cv2.imencode(".png", img)
    # buffer_bytes = encoded_img.tobytes()

    # enhancer(buffer_bytes)