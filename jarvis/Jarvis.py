from calendar import month
from distutils.spawn import spawn
from email import message
from email.message import Message
import imp
from math import remainder
from pydoc_data.topics import topics
from unicodedata import name
from unittest import result
from xmlrpc.client import DateTime
import pyttsx3 #pip install pyttsx3 == text data into speech using pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition From Mic
#import smtplib
#from secrets import senderemail, epwd, to
import pyautogui
import webbrowser as wb
from time import sleep 
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil # pip install psutil
from nltk.tokenize import word_tokenize


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voices = engine.getProperty('voices')
   # print(voices[0].id)
    if voice == 1:
        engine.setProperty('voice',voice[0].id)
        

    if voice == 2:
        engine.setProperty('voice',voice[1].id)
       
   
    speak("Hello sir,How can I help you")#jarvis


def time():
       Time = datetime.datetime.now().strftime("%I:%M:%S")# Hour = I  ,mins = M,S = sec
       speak("the  time is:") 
       speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the  date is:")   
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning sir")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("good night sir")
def wishme():
    speak("Welcome Back sir!")
    speak("hello my name is jarvis")
    time()
    date()
    speak("How can I help you sir?")
    greeting()

   

#while True:
#  voice = int(input('Press 1 for male \n2Press 2 for female'))
#     speak(audio)
#wishme()

def takeCommandCMD():
    query = input("Please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio , language="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Beg you a pardon")
        return "None"
    return query

#def sendEmail(receiver, subject, content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.starttls()
#    server.login(senderemail, epwd)
#    email = EmailMessage()
#    email['From'] = senderemail
#    email['To'] = receiver
#    email['Subject'] = subject
#    email.set_content(content)
#    server.send_messages(email) 
#    server.close()
#sendEmail()


def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

def searchgoogle():
    speak('what are you looking for?')
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)



#http://api.openweathermap.org/data/2.5/weather?q=maharashtra&units=imperial&appid=931550fc290fac3cf93061a42dc86c70

def news():
    newsapi = NewsApiClient(api_key='06a6f3ef0b034860ac82da9e4254f253')
    speak("what topic do you want the news flash about")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("that's it for now i'll update you in some time")  

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered: {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\skidr\\Downloads\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation


    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("ok sir flipping a coin")
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("I flipped the coin and you got"+toss)

def roll():
    speak("ok sir right away")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("i rolled a die and you got"+roll)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent )

if __name__=="__main__":
    speak("hello sir jarvis here")
   # wishme()
    wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if 'time' in query:
                time()
    
            elif 'date' in query:
                date()
        
        # elif 'email' in query:
            #    try:
            #       speak('what should i say:')
            #      content = takeCommandMic()
            #     sendEmail(content)
                #    speak("email sent")
                #except Exception as e:
            #      print(e)
            #     speak("unable to send the email")
                
            elif 'message' in query:# requires whatsapp web !!active!! 
                user_name = {
                    'Subject':'+91 98222 15899'
                }
                try:
                    speak("To whom you want to send this message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("whats the message")
                    message = takeCommandMic()
                    sendwhatsmsg(phone_no,message)
                    speak("message has been send")
                except Exception as e:
                    print(e)
                    speak("unable to send,anything else sir?")

            elif 'wikipedia' in query:
                speak("searching on wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)
            
            elif 'search' in query:
                searchgoogle()

            elif 'youtube' in query:
                speak("what should I play on youtube")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)
            
            elif 'weather' in query:
                city = 'maharashtra'
                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=931550fc290fac3cf93061a42dc86c70'

                res = requests.get(url)
                data = res.json()

                weather = data['weather'] [0] ['main']
                temp = data['main']['temp']
                desp = data['weather'] [0] ['description']
                temp = round((temp - 32) * 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f'weather in {city} city is like')
                speak('temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desp))

            elif 'news' in query:
                news()
            
            elif 'read' in query:
                text2speech()
            
            elif 'covid' in query:
                covid()
            
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('Open','')))
            
            elif 'open code' in query:
                codepath = 'C:\\Users\\skidr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)
            
            elif 'joke' in query:
                speak(pyjokes.get_joke())
            
            elif 'screenshot' in query:
                screenshot()

            elif 'remember that' in query:
                speak("What should i remember")
                data = takeCommandMic()
                speak("you said me to remember that "+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()

            elif 'know' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that"+remember.read())

            elif 'password' in query:
                passwordgen()

            elif 'flip' in query:
                flip()

            elif 'roll' in query:
                roll()

            elif 'cpu' in query:
                cpu()
            
            elif 'offline' in query:
                speak("Jarvis ,here sir ,powering off")
                quit()
         

#takeCommandMic() == "hey jarvis what is the date today" tokenize = ['hey' ,'jarvis', 'what', 'is', 'the', 'date' ,'today']