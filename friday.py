import pyttsx3

import pyjokes

import subprocess as s

import webbrowser

import speech_recognition as sr;

import os

import wikipedia

from datetime import datetime

import requests

from bs4 import BeautifulSoup

from geopy.geocoders import Nominatim

from playsound import playsound


def speak(comand):

    engine=pyttsx3.init('sapi5')

    voices=engine.getProperty('voices')

    engine.setProperty('voice',voices[1].id)

    engine.say(comand)

    engine.runAndWait()


def wishme():

    playsound('C://Users//amanp//Programing//Python//final_63750298a5e9710025f5ab7f_861572.mp3')

    os.system('cls')

    speak('activating friday automation! connecting to satellite number 305! , friday is online sir')

    time=datetime.time(datetime.now())

    if time.hour>=5 and time.hour<=12:

        speak('Good morning sir')

    elif time.hour>12 and time.hour<=15:

        speak('good afternoon sir')

    elif time.hour>15 and time.hour<=17:

        speak('good evening sir')

    else:

        speak('good night sir')

    speak('how may i help you')


def takecomand():

    r=sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)

        audio=r.listen(source)

        try:

            query=r.recognize_google(audio)

            query=query.lower()

        except Exception as e:

            speak("did'nt get that")

            print(e)

            return "None"

    return query


def comands(query):

    if 'youtube' in query:

        speak('opening youtube')

        webbrowser.open('https://www.youtube.com',new=2)

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

    elif 'joke' in query:

        joke=pyjokes.get_joke(category='neutral',language='hi-in')

        speak(joke)

        print(joke)

    elif 'search' in query:

        query=query.replace("search", "")

        speak('According to wikipedia')

        text=wikipedia.summary(query,sentences=2)

        print(query)

        speak(query)

    elif 'your' and 'name' in query:

        speak('My name is friday,your personel assistent')

    elif 'what' and 'do' in query:

        speak('i can open system apps,webpages,search wikipedia etc')

    elif 'created' and 'you' in query:

        speak('i have been created by amanpreet singh')

    elif 'eat' and 'you' in query:

        speak('I eat lots of data')

    elif 'time' in query:

        time=datetime.time(datetime.now())

        speak(time.strftime("%H %M"))

        print('Current time: ',time.strftime("%H %M"))

    elif 'temperature' in query:

        a=input('Enter city: ')

        url = "https://www.google.com/search?q="+"weather"+a

        html = requests.get(url).content

        soup = BeautifulSoup(html, 'html.parser')

        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        data = str.split('\n')
        
        time = data[0]
        
        sky = data[1]

        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        strd = listdiv[5].text

        pos = strd.find('Wind')

        print("Temperature is", temp)
        
        print("Time: ", time)
        
        print("Sky Description: ", sky)

    elif 'date' in query:

        date=datetime.now()

        speak(date.strftime("%D"))

        print('Current date: ',date.strftime("%D"))

    elif 'my' and 'name' and ('change' or 'save') in query:

        name=open('names.txt','w+')

        speak('Enter name')

        names=input('Name: ')

        name.write(names)

        name.close()

    elif 'edge' in query:

        s.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

    elif 'name' and 'my' in query:

        try:

            name=open('name.txt')

            print(name.read())

            name.close()

        except:

            speak("i don't have any name saved")

    elif "None" in query:

        speak('say something to search')

        query=takecomand()

        print('You said: '+query)

        text=wikipedia.summary(query,sentences=2)

        print(text)

        speak(text)

    elif 'latitude' or 'longitude' in query:

        loc = Nominatim(user_agent="GetLoc")

        a=input('Enter city name: ')

        getLoc = loc.geocode(a)

        print(getLoc.address)

        print("Latitude = ", getLoc.latitude)
        
        print("Longitude = ", getLoc.longitude)

    elif 'exit' or 'quit' or 'bye' in query:

        speak('bye sir')

        exit(0)

    else:

        text=wikipedia.summary(query,sentences=2)

        print(text)

        speak(text)


def main():

    wishme()

    while(1):

        speak('say something')

        query=takecomand()

        print('You said: ',query)

        speak('recognizing')

        comands(query)


if __name__=="__main__":

    main()