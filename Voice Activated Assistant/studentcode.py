import pyttsx3, turtle, speech_recognition as sr, threading, pygame, time
from datetime import datetime


class Nova():
    def __init__(self):
        pygame.mixer.init()
        self.event = threading.Event()
        self.voice_thread = threading.Thread(target=self.listen, args=(self.event,), daemon=True)
        self.voice_thread.start()
        self.sfx = pygame.mixer.Sound("bloop.wav")
        self.running = True
        self.last_command = ""
        self.talk = False

    def close(self):
        self.running = False
        self.event.set()
        turtle.bye()

    def speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(text)
        engine.runAndWait()

    def listen(self, event):
        while True:
            if not event.is_set():
                event.wait()
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                try:
                    command = recognizer.recognize_google(audio)
                    self.last_command = command
                except:
                    self.last_command = ""
        
    def main(self):
        window = turtle.Screen()
        t = turtle.Turtle()
        window.bgcolor("#1B1B1B")
        t.hideturtle()
        t.sety(-70)
        t.color("#F0F8FF")
        t.begin_fill()
        window.title("Nova Assistant")
        window.tracer(0)
        window.setup(width=500, height=500)
        t.circle(70)
        t.end_fill()
        window.update()
        try:
            window.cv._rootwindow.protocol("WM_DELETE_WINDOW", self.close)
        except:
            pass

        self.speak("Hi, I am Nova, your personal assistant. Call me whenever you need me!")
        
        while self.running:
            t.teleport(x=0, y=-85)
            while self.talk:
                time.sleep(5)
                self.event.clear()
                if "hello" in self.last_command.lower():
                    self.speak("Hiya! I'm here to help. Ask me anything!")
                elif "name" in self.last_command.lower():
                    self.speak("My name is Nova.")
                elif "date" in self.last_command.lower():
                    dt = datetime.now().date()
                    self.speak(f"The date is: {dt}")
                elif "time" in self.last_command.lower():
                    say_time = datetime.now().strftime("%H:%M")
                    self.speak(f"The time is: {say_time}")
                elif "bye" in self.last_command.lower():
                    self.speak("See you later!")
                    exit()
                self.sfx.play()
                for i in range(90, 70, -1):
                    t.pencolor("#1B1B1B")
                    t.circle(i)
                    time.sleep(0.001)
                    window.update()
                self.talk = False
                break

            if "nova" in self.last_command.lower():
                for i in range(70, 90):
                    t.pencolor("#F0F8FF")
                    t.begin_fill()
                    t.circle(i)
                    time.sleep(0.001)
                    window.update()
                    t.end_fill()
                self.sfx.play()
                self.speak("Yes?")
                self.last_command = ""
                self.talk = True
                self.event.clear()
            self.event.set()
            time.sleep(0.05)

        self.event.clear()
        self.speak("Bye!")

Nova().main()