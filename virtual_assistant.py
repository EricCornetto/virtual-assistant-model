# ========================Virtual Assistant Model =============================
#  *   Virtual Assistant Python.
# =============================================================================
#  *   Created By Eric Theodore Cornetto(Ida Bagus Dwi Putra Purnawa).
#  *   Github (https://github.com/EricCornetto).
# =============================================================================
#  *   GNU General Public License v3.0.
# =============================================================================
#             Python Artificial Intellegence
# =============================================================================

from gtts import gTTS
from time import ctime
import os
import time
import speech_recognition as sr
import webbrowser
import playsound
import sys

class VirtualAssistant():
    def __init__(self,name):
        self.name = name

    def speak(self,AudioString):
        print(AudioString)
        tts = gTTS(text=AudioString,lang='en',slow=False,lang_check=True)
        tts.save('audio.mp3')
        playsound.playsound('audio.mp3')
        os.remove('audio.mp3')

    def recordAudio(self):
        recognize = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print('Listen......')
            recognize.adjust_for_ambient_noise(source)
            audio = recognize.listen(source)

        data = ""

        try:
            data = recognize.recognize_google(audio)
            print("You Said : " + data)
        except sr.UnknownValueError:
            print(self.name + "Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request result from Alice Speech Recognition Service; {0}".format(e))
        return data

    def assistant(self,data):
        if "how are you" in data:
            self.speak("Iam Fine")

        if "what is your name" in data:
            self.speak("My name is " + self.name)

        if "who are you" in data:
            self.speak("Iam a Virtual Assistant")

        if "what time is it" in data:
            self.speak(ctime())

        if "where is" in data:
            data = data.split(" ")
            location = data[1]
            self.speak("Hold on Eric, I will show you where " + location + " is .")
            webbrowser.open("https://www.google.com/maps/place/" + location + "/&amp;")

        if "open browser" in data:
            webbrowser.open("https://www.google.com")

        if "open YouTube" in data:
            webbrowser.open("https://www.youtube.com")

        if "open Facebook" in data:
            webbrowser.open("https://www.facebook.com")

        if "hello Alice" in data:
            self.speak("Hello")

        if "what is your name" in data:
            self.speak("My Name is Alice, iam a Virtual Assistant")

        if "thank you" in data:
            self.speak("Your Welcome")

        if "good morning" in data:
            self.speak("Good Morning")

        if "good night" in data:
            self.speak("Good Night")

        if "goodbye" in data:
            self.speak("Ok goodbye")
            sys.exit()

        if "open Steam" in data:
            self. speak("Ok Open Steam")
            os.startfile('C:\\Program Files (x86)\Steam\Steam.exe')
                
