import pyttsx3

import pyjokes

import subprocess as s

import webbrowser

import speech_recognition as sr;

import os

import wikipedia

from datetime import datetime

import requests

from playsound import playsound

import smtplib

from pprint import pprint

from selenium import webdriver


def speak(comand):

    engine=pyttsx3.init('sapi5')

    voices=engine.getProperty('voices')

    engine.setProperty('voice',voices[0].id)

    engine.say(comand)

    engine.runAndWait()


def wishme():

    playsound('C://Users//amanp//Programing//Python//final_63750298a5e9710025f5ab7f_861572.mp3')

    os.system('cls')

    time=datetime.time(datetime.now())

    speak('welcome back master')

    if time.hour>=5 and time.hour<=12:

        speak('Good morning master')

    elif time.hour>12 and time.hour<=17:

        speak('good afternoon master')

    elif time.hour>17 and time.hour<=19:

        speak('good evening master')


    speak('activating jarvis automation! please wait a moment! all systems are online now sir! i am ready to take commands!')

    speak('how may i help you')


def takecomand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print(f"You Said:{query}\n")

    except Exception as e:

        print(e)

        speak("Say that again Please...")

        return "None"

    return query

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.login('co21308@gmail.com', 'aman09122001')

    server.sendmail('co21308@gmail.com', to, content)

    server.close()


def comands(query):

    if 'youtube' in query:

        speak('opening youtube')

        webbrowser.open('https://www.youtube.com',new=2)

    elif 'how are you' in query:

        speak('i am doing well')

    elif 'gmail' in query:

        speak('opening gmail')

        webbrowser.open('https://www.gmail.com',new=2)

    elif 'sheets' in query:

        speak('opening sheets')

        webbrowser.open('https://docs.google.com/spreadsheets',new=2)

    elif 'google' in query:

        speak('opening google')

        webbrowser.open('htpps://www.google.com',new=2)

    elif 'drive' in query:

        speak('opening drive')

        webbrowser.open('https://www.drive.google.com/drive',new=2)

    elif 'explorer' in query:

        speak('opening explorer')

        os.system('explorer')

    elif 'notepad' in query:

        speak('opening notepad')

        os.system('NOTEPAD')

    elif 'wordpad' in query:

        speak('opening wordpad')

        os.system('WORDPAD')

    elif 'email to gurmehar' and 'send email to gurmehar' in query:

        try:

            speak("What should I say?")

            content = takecomand()

            to = "co21318@gmail.com"

            sendEmail(to, content)

            speak("Email has been sent!")

        except Exception as e:

            print(e)

            speak("Sorry my friend . I am not able to send this email") 

    elif 'show' in query:

        os.system('explorer C://{}'.format(query.replace('Open','')))

    elif 'joke' in query:

        joke=pyjokes.get_joke(category='neutral',language='hi-in')

        speak(joke)

        print(joke)

    elif 'code' in query:

        codePath = "C:\\Users\\amanp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        os.startfile(codePath)

    elif 'search' in query:

        query=query.replace("search", "")

        speak('According to wikipedia')

        text=wikipedia.summary(query,sentences=2)

        print(text)

        speak(text)

    elif 'your' and 'name' in query:

        speak('My name is jarvis,your personel assistent')

    elif 'what' and 'do' in query:

        speak('i can open system apps,webpages,search wikipedia etc')

    elif 'created' in query:

        speak('i have been created by amanpreet singh')

    elif 'eat' in query:

        speak('I eat lots of data')

    elif 'time' in query:

        strTime = datetime.datetime.now().strftime("%I:%M:%S")

        speak(f"Sir, the time is {strTime}")

    elif 'how is the weather' and 'weather' in query:

        url = 'https://api.openweathermap.org/'

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

    elif 'date' in query:

        date=datetime.now()

        speak(date.strftime("%D"))

        print('Current date: ',date.strftime("%D"))

    elif 'browser' in query:

        s.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

    elif 'none' in query:

        query=takecomand().lower()

        print('You said: ',query)

        comands(query)

    elif 'exit' or 'quit' or 'bye' in query:

        speak('bye sir')

        quit()

    else:

        text=wikipedia.summary(query,sentences=2)

        print(text)

        speak(text)


def main():

    wishme()

    while(1):

        query=takecomand().lower()

        print('You said: ',query)

        comands(query)


if __name__=="__main__":

    main()