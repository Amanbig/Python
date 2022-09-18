from datetime import datetime

import os

import pyjokes

import wikipedia

import webbrowser

import requests

from bs4 import BeautifulSoup

from geopy.geocoders import Nominatim

def wishme():

    time=datetime.time(datetime.now())

    if time.hour>=5 and time.hour<12:

        print('Good morning sir')

    elif time.hour>=12 and time.hour<15:

        print('Good afternoon sir')

    elif time.hour>=15 and time.hour<17:

        print('Good evening sir')

    else:

        print('Good night sir')

    print('How may i help you')


def comand(query):

    if 'youtube' in query:

        print('Opening youtube')

        webbrowser.open('https://www.youtube.com',new=2)

    elif 'gmail' in query:

        print('opening gmail')

        webbrowser.open('https://www.gmail.com',new=2)

    elif 'google' in query:

        webbrowser.open('https://www.google.com',new=2)

    elif 'explorer' in query:

        print('Opening explorer')

        os.system('explorer')

    elif 'notepad' in query:

        print('opening notepad')

        os.system('NOTEPAD')

    elif 'time' in query:

        time=datetime.time(datetime.now())

        print('Current time: ',time.strftime('%H %M'))

    elif 'date' in query:

        date=datetime.now()

        print('Current Date: ',date.strftime('%D'))

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

    elif 'search' in query:

        query=query.replace("search", "")

        text=wikipedia.summary(query,sentences=2)

        print(text)

    elif 'who are you' in query:

        print('I am your personel chat bot Siri')

    elif 'what can you do' in query:

        print('I can open websites,explorer,search etc')

    elif 'latitude' or 'longitude' in query:

        loc = Nominatim(user_agent="GetLoc")

        a=input('Enter city name: ')

        getLoc = loc.geocode(a)

        print(getLoc.address)

        print("Latitude = ", getLoc.latitude)
        
        print("Longitude = ", getLoc.longitude)

    elif 'who created you' in query:

        print('I have been created by Amanpreet Singh')

    elif 'joke' in query:

        joke=pyjokes.get_joke(category='neutral',language='en')

        print(joke)

    elif 'quit' or 'exit' or 'bye' in query:

        print('bye sir')

        exit(0)

    elif 'none' in query:

        print('Not get that')


def main():

    wishme()

    while(1):

        query=input('Camand: ')

        comand(query)

main()