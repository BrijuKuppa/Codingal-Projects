import threading
import sys
import time
from time import sleep
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import wave
import speech_recognition as sr
from speech_recognition import AudioData
import datetime

event = threading.Event()

def stop_event():
    input("")
    event.set()

def fancy_print(text: str, time=0.05, color=""):
    for i in text:
        print(i, end="", flush=True)
        sleep(time)
    
def loader():
    loader_text = [
    "●  ", 
    "○  ", 
    "∙  ",  
    "○  ",
]
    i = 0

    while not event.is_set():
        if i == len(loader_text) - 1:
            i = 0
        print(f"\r{loader_text[i]} Recording the audio from your microphone.", flush=True, end="")
        i += 1
        time.sleep(0.2)
    print("🚫 Recording stopped.\n---------------------")

def capture_recording():
    p = pyaudio.PyAudio()

    recording = p.open(format=pyaudio.paInt16, rate=44100, channels=1, input=True, frames_per_buffer=1024)
    frames = []

    input("")
    print("---------------------\n🎤 Started recording...")
    threading.Thread(target=stop_event).start()
    threading.Thread(target=loader).start()

    while not event.is_set():
        try:
            data = recording.read(1024)
            frames.append(data)
        except Exception as e:
            fancy_print(f"\n❌ There was an unexpected error. Please rerun the program. (Debug: {e})")
            break
    
    recording.stop_stream()
    recording.close()
    width = p.get_sample_size(pyaudio.paInt16)

    data = b"".join(frames)
    return data, 44100, width

def find_speech(data, rate, width):
    r = sr.Recognizer()
    audio = AudioData(data, rate, width)
    text = ""
    try:
        text = r.recognize_tensorflow(audio)
    except Exception as e:
        fancy_print(f"\n❌ There was an unexpected error. Please rerun the program. (Debug: {e})")
        exit()
    fancy_print(f"\n✅ Succesfully transcibed! Here is the output: \n {text}")
    now = datetime.datetime.now()
    filename = now.strftime("%m%d%Y-%H%M%S")+".txt"
    with open(filename, "w") as f:
        f.write(str(text))

def show_waves(data, rate):
    data = np.frombuffer(data, dtype=np.int16)
    time = np.linspace(0, len(data) / rate, num=len(data))
    plt.plot(time, data)
    plt.title("Audio from Microphone")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

def save_wave(data, rate, width):
    now = datetime.datetime.now()
    filename = now.strftime("%m%d%Y-%H%M%S")+".wav"
    with wave.open(filename, "wb") as b:
        b.setnchannels(1)
        b.setsampwidth(width)
        b.setframerate(rate)
        b.writeframes(data)

def main():
    fancy_print("\n\n🔃 Loading 'Speech Recognition'")
    fancy_print(".....", 0.7)
    fancy_print("\n✅ Fully Loaded!")
    fancy_print("\n\nPress your 'Enter' key to start recording, and press it again to stop.\n")
    data, rate, width = capture_recording()
    find_speech(data, rate, width)
    show_waves(data, rate)
    save_wave(data, rate, width)
main()