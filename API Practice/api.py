import requests

url = "https://dog.ceo/api/breeds/image/random"

def startup():
    try:
        dog_imgs = requests.get(url, timeout=5)
        dog_imgs.raise_for_status()
    except requests.RequestException as e:
        print(f"There was an unexpected error.\n{e}")
    finally:
        print("\n\nDog Picture Scroll")
        print("(Press enter see more or 'q' quit.)")
        print("-----------------------------")

def get_img():
    while True:
        choice = input(">")
        if choice == "q":
            print("-----------------------------")
            print("Have a paw-sitive day! 🐾\n\n")
            break
        elif choice == "":
            try:
                dog_imgs = requests.get(url, timeout=5)
                dog_imgs.raise_for_status()
                parse = dog_imgs.json()
                message = parse.get("message")
                result = parse.get("status")
                if message and result == "success":
                    print(message)
            except requests.RequestException as e:
                print(f"There was an unexpected error getting the image.\n{e}")

if __name__ == "__main__":
    startup()
    get_img()