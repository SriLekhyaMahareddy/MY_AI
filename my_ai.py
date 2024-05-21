import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import pyscreeze
x = pyttsx3.init()
import json
import requests
import pywhatkit as kit
import smtplib
import song
import os


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmY3NGE4MjgtMDdjYy00YTFjLTk0NmItNDRiYjRjYmI0OTc1IiwidHlwZSI6ImFwaV90b2tlbiJ9.tHoBWmvqVj1OkIN0_a98QmRDCTG7RVZ7EAo5OFF2vJs"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "suggest me a best thriller movie ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "lekhya"
}



def respond(query):
    payload["text"] = query
    #print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])


def speak(audio):
    x.say(audio)
    x.runAndWait()
#speak("hello")

def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    #print(t)
    speak(t)

#time()

def date():
    y = str(datetime.datetime.now().year)
    m = str(datetime.datetime.now().month)
    d =str(datetime.datetime.now().day)
    #print(y)
    speak(d)
    speak(m)
    speak(y)
#date()

def wish():
    speak("Hi Ai")
    hour = datetime.datetime.now().hour
    if hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening Sir")
    speak("How can i help you sir")

#wish()
def inp():
    s1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        s1.pause_threshold=1
        audio = s1.listen(source)
        try:
            print("Recognizing...")
            query = s1.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Repeat Once Again!")
            inp()
            return "None"
        return query
#inp()

def screenshot():
    im1 = pyscreeze.screenshot()
    im2 = pyscreeze.screenshot('C:/python project/image.png')

def youtube(ele):
    kit.playonyt(ele)

def browser(elem):
    kit.search(elem)

def whatsapp(t,msg):
    kit.sendwhatmsg_instantly(t,msg)

def sendEmail(to,msg):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('21pa1a0597@vishnu.edu.in','xgsu dvah xijf zxdd')
    server.sendEmail('21pa1a0597@vishnu.edu.in',to,msg)

#song.play_song(r"C:\Users\sri lekhya\Downloads\pspk.mp3")


if __name__ =="__main__":
    #wish()
    while True:
        query = inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("I am searching ...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "screenshot" in query:
            speak("Taking screenshot...")
            screenshot()
        elif "exit" in query:
            speak("Exiting")
            print("Bye...")
            exit()
        elif "open youtube" in query:
            try:
                speak("what you want to search")
                ele = inp()
                speak("Iam searching")
                youtube(ele)
            except Exception as e:
                print(e)
                speak("failed to open youtube")
        elif "browser" in query:
            try:
                speak("start your browsing")
                elem = inp()
                speak("Browsing")
                browser(elem)
            except Exception as e:
                print(e)
                speak("failed to open browser")
        elif "send whatsapp message" in query:
            try:
                speak("provide Number")
                t=input()
                speak("provide message")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "remember" in query:
            speak("what i have to remember")
            data = inp()
            speak("I will remember "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "anything i have to know" in query:
            remember = open('data.txt','r')
            speak("you said me that"+remember.read())
        elif "email" in query:
            try:
                speak("what do you want to send")
                msg = inp()
                speak("enter receipient email")
                to = input()
                sendEmail(to,msg)
                speak("sent successfully")
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "play song" in query:
            song_path = input("enter song path")
            song.play_song(song_path)
        elif "pause" in query:
            song.controller("pause")
        elif "wait" in query:
            song.controller("unpause")
        elif "plays" in query:
            try:
                song.controller(song_path)
            except:
                print("please say 'play song'")
        elif "stop" in query:
            song.controller("stop")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        else:
            respond(query)
    






