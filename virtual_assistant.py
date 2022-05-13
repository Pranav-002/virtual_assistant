import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os
from PIL import Image
import subprocess
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import PyAudio

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = 'Petra'
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')
        print(">>", voice_data.lower())
        return voice_data.lower()

def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis_obj.name + ":", audio_string)
    os.remove(audio_file)


def respond(voice_data):
    # greeting1
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["Hey, how can I help you " + person_obj.name, "Hey, what's up? " + person_obj.name,
                     "Namaste " + person_obj.name, "How you doin'? " + person_obj.name, "Hello " + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # assistant's name
    if there_exists(["What is your name", "What's your name", "Tell me your name"]):
        if person_obj.name:
            engine_speak("My name is Petra.")
        else:
            engine_speak("I am " + asis_name + ". Who are you?")

    if there_exists(["Your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("Cool, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)

    # user's name
    if there_exists(["My name is", "I am"]):
        try:
            person_name = voice_data.split("is")[-1].strip()
        except:
            person_name = voice_data.split("am")[-1].strip()
        engine_speak("Okay, i will remember that " + person_name)
        person_obj.setName(person_name)

    # greeting2
    if there_exists(["How are you", "How are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # time
    if there_exists(["What's the time", "Tell me the time", "What time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + " minutes"
        engine_speak(time)

    # google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google.")

    # youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on youtube.")

    # price (stock)
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google.")

    # music
    if there_exists(["play"]):
        search_term = voice_data.split("play")[-1]
        url = "https://open.spotify.com/search/" + search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to " + search_term + ".")

    # amazon.com
    if there_exists(["amazon"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.in" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what i found for " + search_term + " on amazon.com.")

    # make a note
    if there_exists(["make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Note taken!")

    # open instagram
    if there_exists(["open instagram"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram...")

    # open twitter
    if there_exists(["open twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter...")

    # time table
    if there_exists(["show my time table"]):
        im = Image.open(r"G:\College\Time Table 8th Sem.jpeg")
        im.show()

    # weather
    if there_exists(["weather", "tell me the weather report", "whats the condition outside", "how's the weather"]):
        try:
            search_term = voice_data.split("weather")[-1]
        except:
            search_term = voice_data.split("report")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found on google")

    # gmail
    if there_exists(["open my mail", "open gmail", "check my email"]):
        try:
            search_term = voice_data.split("mail")[-1]
        except:
            search_term = voice_data.split("gmail")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("opening gmail...")

    # rock paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("Choose among rock paper or scissors")
        moves = ["rock", "paper", "scissors"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        if pmove == cmove:
            engine_speak("its a draw.")
        elif pmove == "rock" and cmove == "scissors":
            engine_speak(person_name + " wins.")
        elif pmove == "rock" and cmove == "paper":
            engine_speak(asis_name + " wins.")
        elif pmove == "paper" and cmove == "rock":
            engine_speak(person_name + " wins.")
        elif pmove == "paper" and cmove == "scissors":
            engine_speak(asis_name + " wins.")
        elif pmove == "scissors" and cmove == "paper":
            engine_speak(person_name + " wins.")
        elif pmove == "scissors" and cmove == "rock":
            engine_speak(asis_name + " wins.")

    # calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+' or opr == "plus":
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-' or opr == "minus":
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == "*" or opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == "/" or opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == "^" or opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    # screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users\prana\OneDrive\Pictures\Screenshots')

    # definition
    if there_exists(["definition of"]):
        definition = record_audio("What do you need the definition to?")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('I\'m sorry i could not find that definition!')
            elif definitions[1]:
                engine_speak('Here is what i found ' + definitions[1])
            else:
                engine_speak('Here is what i found ' + definitions[2])
        else:
            engine_speak("I'm sorry i could not find the definition of " + definition)

    # exit
    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye bye!")
        exit()

time.sleep(1)
person_obj = person()
asis_obj = asis()
asis_obj.name = 'Petra'
engine = pyttsx3.init()

while(1):
    voice_data = record_audio("Recording")
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)