# import speech_recognition as sr
# import pyttsx3
# from deep_translator import GoogleTranslator  # Replaces googletrans

# # Initialize text-to-speech engine
# def speak(text, language="en"):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     voices = engine.getProperty('voices')

#     # Use English voice or fallback
#     if language == "en":
#         engine.setProperty('voice', voices[0].id)
#     else:
#         engine.setProperty('voice', voices[1 % len(voices)].id)

#     engine.say(text)
#     engine.runAndWait()

# # Convert spoken English to text
# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Please speak in English...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         print("🧠 Recognizing...")
#         text = recognizer.recognize_google(audio, language="en-US")
#         print(f"✅ You said: {text}")
#         return text
#     except sr.UnknownValueError:
#         print("❌ Could not understand the audio.")
#     except sr.RequestError as e:
#         print(f"❌ API error: {e}")
#     return ""

# # Translate text using deep-translator
# def translate_text(text, target_language="hi"):
#     translated = GoogleTranslator(source='auto', target=target_language).translate(text)
#     print(f"🌍 Translated text: {translated}")
#     return translated

# # Show language options and return selected code
# def display_language_options():
#     print("\n🌐 Available languages:")
#     print("1. Hindi (hi)")
#     print("2. Tamil (ta)")
#     print("3. Telugu (te)")
#     print("4. Bengali (bn)")
#     print("5. Marathi (mr)")
#     print("6. Gujarati (gu)")
#     print("7. Malayalam (ml)")
#     print("8. Punjabi (pa)")

#     choice = input("Select target language (1–8): ")

#     language_dict = {
#         "1": "hi", "2": "ta", "3": "te", "4": "bn",
#         "5": "mr", "6": "gu", "7": "ml", "8": "pa"
#     }

#     return language_dict.get(choice, "hi")  # Default to Hindi

# # Main program flow
# def main():
#     target_language = display_language_options()
#     original_text = speech_to_text()

#     if original_text:
#         translated_text = translate_text(original_text, target_language=target_language)
#         speak(translated_text, language="en")  # TTS in English voice
#         print("✅ Translation spoken out!")

# if __name__ == "__main__":
#     main()










# import speech_recognition as sr# speech recognition auido of microphone convert to text on terminal
# import pyttsx3 #text convert to speech engine
# from googletrans import Translator  # Google Translate API

# # Initialize text-to-speech engine
# def speak(text, language="en"):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Speed of speech
#     voices = engine.getProperty('voices')

#     # Set voice for English or other language if supported by pyttsx3
#     if language == "en":
#         engine.setProperty('voice', voices[0].id)  # Default English voice
#     else:
#         engine.setProperty('voice', voices[1].id)  # Fallback to another voice if available

#     engine.say(text)
#     engine.runAndWait()

# # Speech-to-Text: Recognize spoken language (English)
# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("🎤 Please speak now in English...")
#         audio = recognizer.listen(source)

#     try:
#         print("🧠 Recognizing speech...")
#         text = recognizer.recognize_google(audio, language="en-US")
#         print(f"✅ You said: {text}")
#         return text
#     except sr.UnknownValueError:
#         print("❌ Could not understand the audio.")
#     except sr.RequestError as e:
#         print(f"❌ API Error: {e}")
#     return ""

# # Translate text using Google Translate API
# def translate_text(text, target_language="es"):  # Default is Spanish
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     print(f"🌍 Translated text: {translation.text}")
#     return translation.text

# # Display language options to the user
# def display_language_options():
#     print("🌐 Available translation languages: ")
#     print("1. Hindi (hi)")
#     print("2. Tamil (ta)")
#     print("3. Telugu (te)")
#     print("4. Bengali (bn)")
#     print("5. Marathi (mr)")
#     print("6. Gujarati (gu)")
#     print("7. Malayalam (ml)")
#     print("8. Punjabi (pa)")

#     choice = input("Please select the target language number (1-8): ")
#     language_dict = {
#         "1": "hi",
#         "2": "ta",
#         "3": "te",
#         "4": "bn",
#         "5": "mr",
#         "6": "gu",
#         "7": "ml",
#         "8": "pa"
#     }
#     return language_dict.get(choice, "es")  # Default to Spanish if input is invalid

# # Main function to combine all steps
# def main():
#     # Step 1: Display language options and get user's choice
#     target_language = display_language_options()

#     # Step 2: Speech-to-Text (recognizing English speech)
#     original_text = speech_to_text()

#     if original_text:
#         # Step 3: Translate to selected target language
#         translated_text = translate_text(original_text, target_language=target_language)

#         # Step 4: Text-to-Speech (Translate output and speak it)
#         speak(translated_text, language="en")  # Speak the translation in English
#         print("✅ Translation spoken out!")

# if __name__ == "__main__":
#     main()











#after class project
import pyttsx3
import random
import datetime

class VoiceMasterPlus:
    def __init__(self):
        """Initialize the TTS engine and configure settings"""
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.current_voice = 0
        self.rate = 150
        self.volume = 1.0

        # Set initial properties
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
        self.engine.setProperty('voice', self.voices[self.current_voice].id)

        # Response templates for personality
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What would you like to talk about?",
            "Greetings! I'm here to help.",
            "Hey! Nice to meet you!"
        ]

        self.farewells = [
            "Goodbye! Have a wonderful day!",
            "See you later! Take care!",
            "Farewell! It was nice talking to you!",
            "Bye! Come back anytime!"
        ]

        self.jokes = [
            "Why did the Python programmer break up with their partner? They had too many arguments!",
            "What do you call a snake that's exactly 3.14 meters long? A π-thon!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "What's a computer's favorite snack? Microchips!",
            "Why was the computer cold? It left its Windows open!"
        ]

        self.motivational_quotes = [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Your limitation—it's only your imagination.",
            "Great things never come from comfort zones."
        ]

    def speak(self, text):
        """Convert text to speech"""
        print(f"🔊 AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def change_voice(self):
        """Toggle between available voices"""
        self.current_voice = (self.current_voice + 1) % len(self.voices)
        self.engine.setProperty('voice', self.voices[self.current_voice].id)
        voice_name = self.voices[self.current_voice].name
        self.speak(f"Voice changed to {voice_name}")

    def adjust_speed(self, action):
        """Increase or decrease speech rate"""
        if action == "faster":
            self.rate = min(300, self.rate + 25)
            self.speak(f"Speed increased to {self.rate}")
        elif action == "slower":
            self.rate = max(50, self.rate - 25)
            self.speak(f"Speed decreased to {self.rate}")
        self.engine.setProperty('rate', self.rate)

    def adjust_volume(self, action):
        """Increase or decrease volume"""
        if action == "louder":
            self.volume = min(1.0, self.volume + 0.2)
            self.speak(f"Volume increased")
        elif action == "quieter":
            self.volume = max(0.2, self.volume - 0.2)
            self.speak(f"Volume decreased")
        self.engine.setProperty('volume', self.volume)

    def tell_time(self):
        """Tell current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"The current time is {time_str}")

    def tell_date(self):
        """Tell current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        self.speak(f"Today is {date_str}")

    def tell_joke(self):
        """Tell a random joke"""
        joke = random.choice(self.jokes)
        self.speak(joke)

    def motivate(self):
        """Share a motivational quote"""
        quote = random.choice(self.motivational_quotes)
        self.speak(quote)

    def repeat_text(self, text):
        """Repeat user's input"""
        self.speak(f"You said: {text}")

    def calculate(self, expression):
        """Perform simple calculations"""
        try:
            result = eval(expression)
            self.speak(f"The answer is {result}")
        except Exception as e:
            self.speak("Sorry, I couldn't calculate that. Please check your expression.")

    def show_commands(self):
        """Display available commands"""
        commands = """
        ╔════════════════════════════════════════════════════════╗
        ║           VOICE MASTER+ COMMANDS                       ║
        ╠════════════════════════════════════════════════════════╣
        ║  hello/hi/hey        - Greet the AI                    ║
        ║  bye/exit/quit       - Exit the program                ║
        ║  change voice        - Switch to different voice       ║
        ║  speak faster/slower - Adjust speech speed             ║
        ║  louder/quieter      - Adjust volume                   ║
        ║  time                - Get current time                ║
        ║  date                - Get current date                ║
        ║  joke                - Hear a random joke              ║
        ║  motivate            - Get motivational quote          ║
        ║  repeat <text>       - AI repeats your text            ║
        ║  calculate <expr>    - Perform calculations            ║
        ║  help/commands       - Show this menu                  ║
        ║  say <anything>      - AI speaks your text             ║
        ╚════════════════════════════════════════════════════════╝
        """
        print(commands)
        self.speak("Commands displayed on screen")

    def process_command(self, command):
        """Parse and execute user commands"""
        command = command.lower().strip()

        # Greeting commands
        if command in ["hello", "hi", "hey", "greetings"]:
            self.speak(random.choice(self.greetings))

        # Exit commands
        elif command in ["bye", "exit", "quit", "goodbye"]:
            self.speak(random.choice(self.farewells))
            return False

        # Voice control
        elif command == "change voice":
            self.change_voice()

        # Speed control
        elif "faster" in command:
            self.adjust_speed("faster")
        elif "slower" in command:
            self.adjust_speed("slower")

        # Volume control
        elif "louder" in command:
            self.adjust_volume("louder")
        elif "quieter" in command:
            self.adjust_volume("quieter")

        # Time and date
        elif command == "time":
            self.tell_time()
        elif command == "date":
            self.tell_date()

        # Entertainment
        elif command == "joke":
            self.tell_joke()
        elif command == "motivate" or command == "motivation":
            self.motivate()

        # Help
        elif command in ["help", "commands"]:
            self.show_commands()

        # Repeat functionality
        elif command.startswith("repeat "):
            text = command.replace("repeat ", "")
            self.repeat_text(text)

        # Calculate
        elif command.startswith("calculate "):
            expression = command.replace("calculate ", "")
            self.calculate(expression)

        # Say anything
        elif command.startswith("say "):
            text = command.replace("say ", "")
            self.speak(text)

        # Default response for unknown commands
        else:
            responses = [
                "I didn't understand that command. Try saying 'help' for available commands.",
                "Sorry, I don't know that command. Type 'commands' to see what I can do.",
                "I'm not sure what you mean. Say 'help' to see all my features."
            ]
            self.speak(random.choice(responses))

        return True

    def run(self):
        """Main program loop"""
        print("\n" + "="*60)
        print("🎙️  VOICE MASTER+ - Extended Talking AI")
        print("="*60)
        self.speak("Welcome to Voice Master Plus! I'm your interactive talking AI assistant.")
        self.speak("Type 'help' to see all available commands.")
        print("\n💡 Tip: Type 'help' to see all commands\n")

        while True:
            try:
                user_input = input("👤 You: ").strip()

                if not user_input:
                    continue

                if not self.process_command(user_input):
                    break

            except KeyboardInterrupt:
                print("\n")
                self.speak("Program interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                self.speak("An error occurred. Please try again.")

# Run the application
if __name__ == "__main__":
    app = VoiceMasterPlus()
    app.run()