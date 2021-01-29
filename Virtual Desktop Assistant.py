from tkinter import * 
#Tkinter is the standard GUI library for Python. 
# Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit. ... 
#Create the GUI application main window.

from PIL import ImageTk,Image 
# PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
import turtle #turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas.

import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python

import speech_recognition as sr 
#Speech recognition, also known as automatic speech recognition (ASR), 
#computer speech recognition, or speech-to-text, is a capability which enables a program to process human speech into a written format.
import datetime #This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.

import wikipedia #Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
import webbrowser #The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.

import os #The design of all built-in operating system dependent modules of Python is ... operating system are also available through the os module,
import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

import random  #You can generate random numbers in Python by using random module. Python offers random module that can generate random numbers. 






print("Harii is starting")

sir="Harii"

engine = pyttsx3.init()
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
        
    except :
        # print (e)

        print ("Say that again please sir...")
        speak("Say that again please sir...")
        return "None"


class Run():
    def __init__(self): #def __init__(self) -> None: ...
        root=Tk()
        root.title('Harii')
        root.geometry('1280x720')

        img=ImageTk.PhotoImage(Image.open(r'D:\im.png'))
        panel=Label(root,image=img)
        panel.pack(side='right',fill='both',expand='no')

        compText=StringVar()
        self.userText=StringVar()

        self.userText.set('click \'Run Harii\' to Give command')

        userFrame=LabelFrame(root,text='User',font=('Black ops one',10,'bold'))
        userFrame.pack(fill='both',expand='yes')

        left=Message(userFrame,textvariable= self.userText, bg='#33CFFF',fg='black')
        left.config(font=("Century Gothic",24,'bold'))
        left.pack(fill='both', expand='yes')

        compFrame=LabelFrame(root,text="Harii",font=('Black ops one',10,'bold'))
        compFrame.pack(fill='both',expand='yes')

        left2=Message(compFrame,textvariable= compText, bg='#FF0000',fg='black')
        left2.config(font=("Century Gothic",24,'bold'))
        left2.pack(fill='both', expand='yes')

        compText.set('I am Harii Sir, PLease tell me how may I help you')
        Button(root,text='Run Hari',font=('Black ops one',10,'bold'),bg='#800000',fg='white',command=self.clicked).pack(fill='x',expand='no')
        Button(root,text='Close',font=('Black ops one',10,'bold'),bg='#800000',fg='white',command=root.destroy).pack(fill='x',expand='no')


        root.mainloop()

    def clicked(self):
        print("Working..")
        query=takeCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
        if 'wikipedia' in query:
            # logic for excute the takes based on query
            #  if  'Wikipedia' in query:
            # print("hii")
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe%s'
            webbrowser.get(chrome_path).open("wikipedia.org")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'youtube' in query:
            chrome_path ='C:/Program Files/Google/Chrome/Application/chrome.exe%s'
            webbrowser.get(chrome_path).open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com") 
        elif 'music' in query:
            n = random.randint(0,100)
            print(n)
            music_dir = 'D:\\hari\\bhajan 1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\hario\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            



if __name__ == "__main__":
        WishMe()
        widget=Run()
      
       


