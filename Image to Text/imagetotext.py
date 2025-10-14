import requests
import io, os
from PIL import Image
from tkinter import *
from tkinter import messagebox
from random import randint

def request(api_key, image, caption=""):
    headers = {"Authorization" : f"Bearer {api_key}"}
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    if caption == "": 
        output = requests.post("https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning", headers=headers, json=buffer)
        return output.json()[0]["generated_text"]
    elif caption != "": 
        output = requests.post("https://api-inference.huggingface.co/models/gpt2", headers=headers, json={"inputs" : f"Expand this caption into 30 words {caption}", "parameters" : {"max_new_tokens" : 50}})
        return output.json()

def check_path(path):
    if not path or not os.path.isfile(path): 
        messagebox.showwarning("Invalid", "Your path was invalid.")
        return False
    try: 
        Image.open(path)
        return path
    except Exception as e:
        messagebox.showwarning("Error", f"There was an unexpected error. {e}")
        return False

def output(path, choice):
    path = check_path(path)

    if path != False:
        result_window = Toplevel()
        try:
            image = Image.open(path)
            result_text = request("", image)
            precise_text = request("", image, caption=result_text)
            if choice == "basic":
                result = Label(result_window, text=f"Ouput: \n{result_text}", font=("Arial", 30, "bold"))
                result.pack(expand=True)
            elif choice == "precise":
                result = Label(result_window, text=f"Ouput: \n{precise_text}", font=("Arial", 30, "bold"))
                result.pack(expand=True)
        except Exception as e:
            error = Label(result_window, text=f"Oh snap! Something went wrong. \n{e}", font=("Arial", 30, "bold"))
            error.pack(expand=True)

def guidisplay():
    root = Tk()
    root.geometry("800x500")
    root.title("Image Caption Generator")

    label = Label(root, text="Welcome to Image Caption Generator!", font=("Arial", 30, "bold"), foreground="green")

    def main_window():
        root.destroy()
        window = Tk()
        menu = Menu(window)
        helpmenu = Menu(menu)
        window.config(menu=menu)
        window.geometry("800x500")
        window.title("Image Caption Generator")

        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="How to Use")
        selected_choice = StringVar()
        entry_str = StringVar()
        path = Entry(window, width=100, textvariable=entry_str)
        btn = Button(window, text="Generate", height=5, width=50, font=("Arial", 15, "bold"), foreground="blue", command=lambda: output(entry_str.get(), selected_choice.get()))
        choice1 = Radiobutton(window, text="Basic Summary", variable=selected_choice, value="basic", font=("Arial", 20, "bold"))
        choice2 = Radiobutton(window, text="Precise Summary", variable=selected_choice, value="precise", font=("Arial", 20, "bold"))

        path.insert(0, "Enter your path here.")
        path.pack(pady=50)
        choice1.pack(pady=10)
        choice2.pack(pady=10)
        btn.pack(pady=10)

        def color_change():
            c1, c2, c3 = randint(0, 255), randint(0, 255), randint(0, 255)
            btn.config(foreground=f"#{c1:02x}{c2:02x}{c3:02x}")
            window.after(300, color_change)
        color_change()
        print(selected_choice.get())

        window.mainloop()

    btn = Button(root, text="Continue", height=10, width=80, font=("Arial", 30, "bold"), foreground="blue", border=False, command=main_window)

    label.pack(pady=20)
    btn.pack(pady=100)
    root.mainloop()


if __name__ == "__main__":
    guidisplay()