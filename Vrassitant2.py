
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from datetime import datetime
from functions.os_ops import open_calculator
import operator


#Virtual Artificial Entity for Robust Operational Support
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen(timeout=5):
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('Listening...')
        try:
            audio = listener.listen(source, timeout=timeout)
            command = listener.recognize_google(audio)
            command = command.lower()
            print('User Command:', command)
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
    return command


def play_song(song):
    talk('Playing ' + song)
    pywhatkit.playonyt(song)


def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    talk('The current time is ' + current_time)


def get_person_info(person):
    try:
        info = wikipedia.summary(person, sentences=1)
        print('Person Info:', info)
        talk(info)
    except wikipedia.exceptions.WikipediaException:
        talk('Sorry, I could not find any information about ' + person)


def tell_joke():
    joke = pyjokes.get_joke()
    print('Joke:', joke)
    talk(joke)


def search_internet(query):
    talk('Searching the internet for ' + query)
    query = query.replace('alexa', '')
    webbrowser.open_new_tab('https://www.google.com/search?q=' + query)


def perrform_Calculation(num1, num2, operator):
    try:
        result = operators[operator](num1, num2)
        talk('The result is ' + str(result))
    except ZeroDivisionError:
        talk('Error: Division by zero')
    except KeyError:
        talk('Invalid operator')


def run_virtual_assistant():
    while True:
        command = listen()
        if command is not None:
            if 'play' in command:
                song = command.replace('play', '')
                play_song(song.strip())
            elif 'current time' in command:
                get_current_time()
            elif 'who the heck is' in command:
                person = command.replace('who the heck is', '')
                get_person_info(person.strip())
            elif 'date' in command:
                talk('Sorry, I have a headache')
            elif 'are you single' in command:
                talk('I am in a relationship with Wi-Fi')
            elif 'joke' in command:
                tell_joke()
            elif 'Search' in command:
                search_internet(command)
            elif 'open calculator' in command:
                open_calculator()
            elif 'calculate' in command:
                command = command.replace('calculate', '').strip()
                parts = command.split()
                if len(parts) == 3:
                    num1 = float(parts[0])
                    operator = parts[1]
                    num2 = float(parts[2])
                    perrform_Calculation(num1, num2, operator)
                else:
                    talk('Invalid calculation. Please provide a valid calculation.')
            else:
                talk('Sorry, I did not understand that command.')
        else:
            talk('Please say the command again.')


run_virtual_assistant()
