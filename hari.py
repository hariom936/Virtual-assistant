import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternnon!")

    else:
        speak("Good Evening!")
    speak("I am Harii Sir, PLease tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and returns String output 

    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening....")
         
        # minimum seconds of speaking audio before  we consider the speaking audio a phase-
        # valuse below this are ignored (for filtering out clicks and pops)

        r.pause_threshold = 1
        audio = r.listen(Source)
    try:
        print("Recognizing....")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{ query}\n")
        return query
    except:

    # print (e)

        print ("Say that again please...")
        speak("Say that again please...")
        return "None"


def main():
        WishMe()
        # while  True:
        if 1:
            query = takeCommand()
            query = query.lower()
            if 'wikipedia' in query:
            # logic for excute the takes based on query
            #  if  'Wikipedia' in query:
            # print("hii")
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results =  wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'youtube' in query:
                webbrowser.open("youtube.com")
            elif 'google' in query:
                webbrowser.open("google.com")
            elif 'stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'music' in query:
                n = random.randint(0,100)
                print(n)
                music_dir = 'D:\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[n]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the is {strTime}")
            elif 'open code' in query:
                codePath = "C:\\Users\\Sanskar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

main()            