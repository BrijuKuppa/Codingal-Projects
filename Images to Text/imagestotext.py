import requests
import io, os
import PIL.Image

def request(api_key, image, caption=""):
    headers = {"Authorization" : f"Bearer {api_key}"}
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    if caption == "": 
        output = requests.post("https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning", headers=headers, data=buffer.getvalue())
        return output.json()[0]["generated_text"]
    elif caption != "": 
        output = requests.post("https://api-inference.huggingface.co/models/gpt2", headers=headers, json={"inputs" : f"Expand this caption into 30 words {caption}", "parameters" : {"max_new_tokens" : 50}})
        return output.json()


def check_path(path):
    if not path or not os.path.isdir(path): 
        print("Your path was invalid.")
        return False
    try: 
        files = os.listdir(path)
        for i in files:
            PIL.Image.open(i)
    except Exception as e:
        print(f"There was an unexpected error. {e}")
        return False


def output(path, choice="basic"):
    path = check_path(path)

    if path != False:
        files = [i for i in os.listdir(path) if i.lower().endswith((".jpg",".png",".jpeg"))]
        try:
            for i in files:
                image_path = os.path.join(path, i)

                for image in open(image_path, "rb"):
                    result_text = request("", image)
                    precise_text = request("", image, caption=result_text)
                    if choice == "basic":
                        print(f"Output: \n{result_text}")
                    elif choice == "precise":
                        print(f"Output: \n{precise_text}")
        except Exception as e:
            error = print(f"Oh snap! Something went wrong. \n{e}")
    if path == False:
        print("\nThere was something wrong with the path. We are now using the defualt images.")
        files = os.listdir("Images")
        try:
            for i in files:
                image_path = os.path.join(path, i)

                for image in open(image_path, "rb"):

                    try:
                        result_text = request("", image)
                    except Exception as e:
                        print(f"Oh snap! Something went wrong. \n(Debug: {e})")
                    try:
                        precise_text = request("", image, caption=result_text)
                    except Exception as e:
                        print(f"Oh snap! Something went wrong. \n(Debug: {e})")

                    if choice == "basic":
                        print(f"Output: \n{result_text}")
                    elif choice == "precise":
                        print(f"Output: \n{precise_text}")
        except Exception as e:
            print(f"Oh snap! Something went wrong. \n(Debug: {e})")


def main():
    print("\n\nStarting 'Images to Text'...")
    folder = input("\nTo get started, put the path for you folder of images. ")
    choice = input("To continue, choose either a basic summary or a concise summary. ")

    if choice.lower().strip() == "basic" or choice.lower().strip() == "concise":
        output(folder, choice=choice)
    else:
        output(folder)


if __name__ == "__main__":
    main()