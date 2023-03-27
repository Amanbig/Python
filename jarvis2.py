import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning AK47!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon AK47!")

    elif hour>=18 and hour<24:
        speak("Good Evening AK47!")

    else:
        speak("Good Night AK47!")

    speak("Jarvis at your Service. Please tell me how can I help You ")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content)
    server.close()

            

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to aman' and 'send email to aman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "co21308@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email") 

        elif 'email to gurmehar' and 'send email to gurmehar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "co21318@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")      

        elif 'open code' in query:
            codePath = "C:\\Users\\amanp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        if 'youtube' in query:
            speak('opening youtube')
            wb.open('https://www.youtube.com',new=2)

        elif 'gmail' in query:
            speak('opening gmail')
            wb.open('https://www.gmail.com',new=2)

        elif 'sheets' in query:
            speak('opening sheets')
            wb.open('https://docs.google.com/spreadsheets',new=2)

        elif 'google' in query:
            speak('opening google')
            wb.open('htpps://www.google.com',new=2)

        elif 'drive' in query:
            speak('opening drive')
            wb.open('https://www.drive.google.com/drive',new=2)

        elif 'explorer' in query:
            speak('opening explorer')
            os.system('explorer')
            
        elif 'notepad' in query:
            speak('opening notepad')
            os.system('NOTEPAD')

        elif 'wordpad' in query:
            speak('opening wordpad')
            os.system('WORDPAD')

        elif 'joke' in query:
            joke=pyjokes.get_joke(category='neutral',language='hi-in')
            speak(joke)
            print(joke)

        elif 'edge' in query:
            os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

        elif 'search' in query:
            query=query.replace("search", "")
            speak('According to wikipedia')
            text=wikipedia.summary(query,sentences=2)
            print(query)
            speak(query)

        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        elif 'name' and 'my' in query:
            try:
                name=open('name.txt')
                print(name.read())
                name.close()
            except:
                speak("i don't have any name saved")

        elif 'go offline' in query:
            speak("ok sir shutting down the system")
            quit()

        
