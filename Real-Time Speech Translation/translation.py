import speech_recognition as sr, tkinter as tk, threading
from deep_translator import GoogleTranslator

window = tk.Tk()
window.title("Translator")
window.geometry("600x500")

frame = tk.Frame(window)
frame.pack()
tk.Label(frame, text="Select a language to translate from:", font=("Arial", 16, "bold"), ).pack(pady=20, padx=20)

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Dutch": "nl",
    "Swahili": "sw",
    "Turkish": "tr"
}

listen_event = threading.Event()
def listen(stop, from_lang, to_lang):
    global words
    global translated
    translated = ""
    words = ""
    while not stop.is_set():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                words += command

                translated += GoogleTranslator(source=from_lang, target=to_lang).translate(words)
            except:
                return

def main(from_lang, to_lang):
    listen_thread = threading.Thread(target=listen, args=(listen_event, languages[from_lang], languages[to_lang]))

    for i in frame.winfo_children():
        i.destroy()

    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏",]
    
    text = tk.Label(frame, text="Listening...", font=("Arial", 16, "bold"))
    text.pack(pady=20)
    
    loader = tk.Label(frame, text="", font=("Arial", 250, "bold"))
    loader.pack(pady=50)

    def loader_func(count=0):
        if count < 100:
            loader.config(text=frames[count % len(frames)])
            window.after(50, loader_func, count + 1)
            window.update_idletasks()

    listen_thread.start()
    loader_func()  
    listen_event.clear()
    print()
    window.after(5000, lambda : 
                ([i.destroy() for i in frame.winfo_children()], 
                tk.Label(
                    frame, 
                    text=f"Original ({from_lang}): {words}\n\n----------------------------------\n\nTranslated to {to_lang}: {translated}", 
                    font=("Arial", 16, "bold")
                    ).pack(pady=150, padx=15)))

for from_lang in languages:
    btn = tk.Button(
        frame,
        text=from_lang,
        command=lambda lang1=from_lang : (
            [i.destroy() for i in frame.winfo_children()],
            tk.Label(
                frame,
                text="Select a language to translate to:",
                font=("Arial", 16, "bold")
            ).pack(pady=20, padx=20),
            [tk.Button(
                frame,
                text=to_lang,
                command=lambda lang2=to_lang : main(lang1, lang2)
            ).pack() for to_lang in languages]
        )
    ).pack()

window.mainloop()