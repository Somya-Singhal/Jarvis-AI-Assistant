from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good afternoon!')
    else:
        speak('Good evening!')

    speak('Hello, I am Jarvis, Please tell me how may I help you?')

def takeCommand():
    # Takes input from the user and returns the string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('somyasinghal321@gmail.com', 'a@bcdefghij')
    server.sendmail('somyasinghal321@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing different tasks

        # Searching any information from wikipedia
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # To open the youtube    
        elif 'open youtube' in query:    
            webbrowser.open("youtube.com")

        # To open the google    
        elif 'open google' in query:    
            webbrowser.open("google.com")

        # To open the stackoverflow    
        elif 'open stackoverflow' in query:    
            webbrowser.open("stackoverflow.com")

        # To tell time    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # To open visual studio code
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # To open microsoft word
        elif 'open microsoft word' in query:
            wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordPath)

        #To send email
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "somyasinghal321@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                speak("Sorry, I am not able to send the email.")    
