import pyttsx3, random, texts, sys, keyboard, time, os, threading, queue, datetime

class HyperSynaptic_Processing_Unit:

    def __init__(self) -> None:
        # self.q = queue.Queue()
        self.engine = pyttsx3.init()
        self.accent = self.engine.getProperty("voices")
        self.current_accent = 0
        self.rate = 150
        self.volume = 1.0

        self.engine.setProperty("voice", self.accent[self.current_accent].id)
        self.engine.setProperty("volume", self.volume)
        self.engine.setProperty("rate", self.rate)

        # threading.Thread(target=self.audio_loop).start()

    # def audio_loop(self):
    #     while True:
    #         text = self.q.get()
    #         self.engine.say(text)
    #         self.engine.runAndWait()

    # def speak(self, text):
    #     self.q.put(text)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def tui(self, type: int):
        intro = """
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │  [ Settings ]   [ Talk ]   [ Leave ]                         │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """

        settings = """
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """

        talk = """
    ┌──────────────────────────────────────────────────────────────┐
    │  Lets Talk                                                   │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome to the HyperSynaptic Processing Unit Talk Menu!     │
    │                                                              │
    │  Commands:                                                   │
    │    [ Hello ]      : I'll say a greeting.                     │
    │    [ Bye ]        : Exit the assistant.                      │
    │    [ Settings ]   : Head to settings menu.                   │
    │    [ Time ]       : Current time.                            │
    │    [ Date ]       : Current date.                            │
    │    [ Joke ]       : Listen to a joke!                        │
    │    [ Motivate ]   : Get motivated.                           │
    │    [ Repeat ... ] : I'll say whatever you type!              │
    │    [ Do ... ]     : I'll calculate whatever you type!        │
    │                                                              │
    │  Type a command below:                                       │    
    """

        if type == 1:
            state = 0
            os.system("cls")
            sys.stdout.write("\033[H")
            print(intro)
            while True:
                if keyboard.is_pressed("left"): 
                    state -= 1
                    if state > 2: state = 0
                    elif state < 0: state = 2

                    if state == 0:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │ [  Settings  ]  [ Talk ]   [ Leave ]                         │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                
                    elif state == 1:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │  [ Settings ]  [  Talk  ]  [ Leave ]                         │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                        
                    elif state == 2:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │  [ Settings ]   [ Talk ]  [  Leave  ]                        │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                    
                    time.sleep(0.15)
                elif keyboard.is_pressed("right"): 
                    state += 1
                    if state > 2: state = 0
                    elif state < 0: state = 2

                    if state == 0:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │ [  Settings  ]  [ Talk ]   [ Leave ]                         │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                
                    elif state == 1:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │  [ Settings ]  [  Talk  ]  [ Leave ]                         │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                        
                    elif state == 2:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  You are using: HyperSynaptic Processing Unit                │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome User! Use the arrow keys to navigate.               │
    ├──────────────────────────────────────────────────────────────┤
    │  Welcome!                                                    │
    │  What would you like to do today?                            │
    │                                                              │
    │  [ Settings ]   [ Talk ]  [  Leave  ]                        │
    │                                                              │
    │  Disclaimer:                                                 │
    │   This content is for informational purposes only.           │
    │   Use at your own risk.                                      │
    └──────────────────────────────────────────────────────────────┘
        """)
                
                    time.sleep(0.15)
                elif keyboard.is_pressed("enter"):
                    time.sleep(0.05)
                    return state

        if type == 2:
            state = 0
            os.system("cls")
            sys.stdout.write("\033[H")
            print(settings)
            while True:
                if keyboard.is_pressed("left"):
                    state -= 1
                    if state > 5: state = 0
                    elif state < 0: state = 5
                    if state == 0:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │    [  Change Accent  ]                                       │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 1:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │    [  Increase Volume  ]                                     │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 2:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │    [  Decrease Volume  ]                                     │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 3:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │    [  Increase Speed  ]                                      │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 4:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │    [  Decrease Speed  ]                                      │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 5:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │    [  Return  ]                                              │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)            
                
                    time.sleep(0.15)
                elif keyboard.is_pressed("right"):
                    state += 1
                    if state > 5: state = 0
                    elif state < 0: state = 5
                    if state == 0:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │    [  Change Accent  ]                                       │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 1:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │    [  Increase Volume  ]                                     │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 2:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │    [  Decrease Volume  ]                                     │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 3:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │    [  Increase Speed  ]                                      │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 4:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │    [  Decrease Speed  ]                                      │
    │                                                              │
    │  4. Other                                                    │
    │     [ Return ]                                               │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)

                    elif state == 5:
                        sys.stdout.write("\033[H")
                        print("""
    ┌──────────────────────────────────────────────────────────────┐
    │  Settings                                                    │
    ├──────────────────────────────────────────────────────────────┤
    │  1. Voice Accent                                             │
    │     [ Change Accent ]                                        │
    │                                                              │
    │  2. Volume                                                   │
    │     [ Increase Volume ]                                      │
    │     [ Decrease Volume ]                                      │
    │                                                              │
    │  3. Speed Accent                                             │
    │     [ Increase Speed ]                                       │
    │     [ Decrease Speed ]                                       │
    │                                                              │
    │  4. Other                                                    │
    │    [  Return  ]                                              │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """)
                
                    time.sleep(0.15)
                elif keyboard.is_pressed("enter"):
                    time.sleep(0.05)
                    return state

        if type == 3:
            os.system("cls")
            sys.stdout.write("\033[H")
            print(talk, end="")
            command = ""
            command = input("│  > ")
            print("    └──────────────────────────────────────────────────────────────┘")
            return command

    def settings(self):
        while True:
            settings = self.tui(2)
            if settings == 0:
                self.current_accent = (self.current_accent + 1) % (len(self.accent))
                self.engine.setProperty("voice", self.accent[self.current_accent].id)
                self.speak("I have a different accent now.")
            elif settings == 1:
                self.volume = min(1.0, self.volume + 0.1)
                self.engine.setProperty("volume", self.volume)
                self.speak("I will talk louder now.")
            elif settings == 2:
                self.volume = max(0.1, self.volume - 0.1)
                self.engine.setProperty("volume", self.volume)
                self.speak("I will talk quieter now.")
            elif settings == 3:
                self.rate = min(300, self.rate + 25)
                self.engine.setProperty("rate", self.rate)
                self.speak("I will talk faster now.")
            elif settings == 4:
                self.rate = max(50, self.rate - 25)
                self.engine.setProperty("rate", self.rate)
                self.speak("I will talk slower now.")
            elif settings == 5:
                break

    def commands(self):
        while True:
            talk = self.tui(3).strip().lower()
            if "hello" in talk or "hi" in talk or "hey" in talk or "greetings" in talk:
                self.speak(random.choice(texts.greetings))
            elif "bye" in talk or "farewell" in talk or "goodbye" in talk or "see you" in talk or "have a nice day" in talk:
                self.speak(random.choice(texts.farewells))
                break
            elif "settings" in talk:
                self.settings()
            elif "time" in talk:
                self.speak(f"The current time is: {datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)}")
            elif "date" in talk:
                self.speak(f"The current date is: {datetime.date.today()}")
            elif "joke" in talk:
                self.speak(random.choice(texts.jokes))
            elif "motivate" in talk:
                self.speak(random.choice(texts.motivational_quotes))
            elif talk.startswith("repeat "):
                repeat = talk.replace("repeat ", "", 1)
                self.speak(repeat)
            elif talk.startswith("do "):
                do = talk.replace("do ", "", 1)
                try:
                    answer = eval(do)
                    self.speak(f"Here is my answer: {answer}")
                except:
                    self.speak("Your expression is invalid.")
            else:
                pass

    def main(self):
        while True:
            main_menu = self.tui(1)
            if main_menu == 0:
                self.settings()
            elif main_menu == 1:
                self.commands()
            elif main_menu == 2:
                os.system("cls")
                return
            
ai = HyperSynaptic_Processing_Unit()
ai.main()