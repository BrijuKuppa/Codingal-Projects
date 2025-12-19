import pyttsx3, turtle, speech_recognition as sr, threading, pygame, time, texts, random
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

        self.engine = pyttsx3.init()
        self.accent = self.engine.getProperty("voices")
        self.current_accent = 0
        self.rate = 150
        self.volume = 1.0

        self.engine.setProperty("voice", self.accent[self.current_accent].id)
        self.engine.setProperty("volume", self.volume)
        self.engine.setProperty("rate", self.rate)

    def close(self):
        self.running = False
        self.event.set()
        turtle.bye()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

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
        turtle_text = turtle.Turtle()
        window.bgcolor("#1B1B1B")

        t.hideturtle()
        turtle_text.hideturtle()

        turtle_text.sety(-150)
        turtle_text.setx(-50)
        turtle_text.color("#F0F8FF")
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
                turtle_text.write(f"You: {self.last_command}")

                if "hello" in self.last_command.lower():
                    self.speak(random.choice(texts.greetings))
                elif "name" in self.last_command.lower():
                    self.speak("My name is Nova.")
                elif "date" in self.last_command.lower():
                    dt = datetime.now().date()
                    self.speak(f"The date is: {dt}")
                elif "time" in self.last_command.lower():
                    say_time = datetime.now().strftime("%H:%M")
                    self.speak(f"The time is: {say_time}")
                elif "joke" in self.last_command.lower():
                    self.speak(random.choice(texts.jokes))
                elif "motivate" in self.last_command.lower():
                    self.speak(random.choice(texts.motivational_quotes))
                elif "calculate" in self.last_command.lower():
                    eq = self.last_command.replace("calculate ", "")
                    try:
                        result = eval(eq)
                        self.speak(f"I got: {result}")
                    except:
                        self.speak("I didn't quite get that.")
                elif "louder" in self.last_command.lower():
                    self.volume = min(1.0, self.volume + 0.1)
                    self.engine.setProperty("volume", self.volume)
                    self.speak("I will talk louder now.")
                elif "quieter" in self.last_command.lower():
                    self.volume = max(0.1, self.volume - 0.1)
                    self.engine.setProperty("volume", self.volume)
                    self.speak("I will talk quieter now.")
                elif "change accent" in self.last_command.lower():
                    self.current_accent = (self.current_accent + 1) % (len(self.accent))
                    self.engine.setProperty("voice", self.accent[self.current_accent].id)
                    self.speak("I have a different accent now.")
                elif "faster" in self.last_command.lower():
                    self.rate = min(300, self.rate + 25)
                    self.engine.setProperty("rate", self.rate)
                    self.speak("I will talk faster now.")
                elif "slower" in self.last_command.lower():
                    self.rate = max(50, self.rate - 25)
                    self.engine.setProperty("rate", self.rate)
                    self.speak("I will talk slower now.")
                elif "bye" in self.last_command.lower():
                    self.speak(random.choice(texts.farewells))
                    exit()

                self.sfx.play()
                for i in range(90, 70, -1):
                    t.pencolor("#1B1B1B")
                    t.circle(i)
                    time.sleep(0.001)
                    window.update()
                turtle_text.clear()
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

if __name__ == "__main__" : Nova().main()