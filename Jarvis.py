import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from nltk.corpus import wordnet
from GoogleTranslate import trans
from PortFolio import describeMe
from JokesAPI import get_random_joke
from WeatherAPI import get_weather_data
from PyCricbuzz import current_match_status

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am Jarvis, how may I help you?')


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception:
        print('Please, say that again...')
        return 'None'

    return query


if __name__ == '__main__':
    # wishMe()

    while True:
        query = takeCommand().lower()
        exitQuery = ['exit', 'quit']
        synoQuery = ['synonyms', 'synonym']
        antoQuery = ['antonyms', 'antonym']

        if 'who am i' in query:
            speak('Welcome Akshay, what do you want to know?')
            query = takeCommand().lower()
            speak(describeMe(query))

        elif 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            speak('Searching through wikipedia...')
            searchResult = wikipedia.summary(query, sentences=2)
            print(searchResult)
            speak('According to wikipedia...')
            speak(searchResult)

        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'play music' in query:
            music_path = 'E:\\Music\\Anupam Roy'
            songs = os.listdir(music_path)
            print(songs)
            os.startfile(os.path.join(music_path, songs[0]))

        elif 'the time' in query:
            speak(datetime.datetime.now().strftime('%H:%M:%S'))

        elif 'say' in query:
            query = query.replace('say', '')
            speak(query)

        elif 'translate' in query:
            qList = list(query.split(' '))
            qList.pop(0)
            qList.pop(0)
            dst = qList.pop(0)
            translateResult = trans(''.join(qList), dst)
            print(translateResult)
            speak(translateResult)

        elif any([q in query for q in synoQuery]):
            word = query[-1]
            synonyms = []
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())

            print(set(synonyms))

        elif any([q in query for q in antoQuery]):
            word = query[-1]
            antonyms = []
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())

            print(set(antonyms))

        elif 'tell' in query and 'joke' in query:
            joke = get_random_joke()
            speak(joke['setup'])
            speak(joke['punchline'])

        elif 'weather' in query:
            speak(get_weather_data(query.split()[-1]))

        elif 'score' in query:
            speak(current_match_status())

        elif any([q in query for q in exitQuery]):
            speak('Goodbye')
            exit()
