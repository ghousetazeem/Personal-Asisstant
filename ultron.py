
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import requests
from bs4 import BeautifulSoup
import pyowm
import json 
import PyPDF2
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import shutil
import PyPDF2

from requests import get


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


rates ={'slow':100 , 'medium':200 , "fast":300}
r = 'fast'
print(rates[r])

engine.setProperty('voices',voice_id)

# engine.setProperty('rate', rates[r] )





#tts
def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()



# speech recognition
def takeCommand():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold=3
            audio = r.listen(source,timeout=5,phrase_time_limit=5)

            print("Recognizing...")
            query = r.recognize_google(audio , language='en-in')
            print(f"user said: {query}") 
            query=query.lower()  
            # speak(query)

    except Exception as e:
        # speak("Say that again please...")
        return "none"
    return query         
   
def wish():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Ultron sir, please tell me what to do")            

def remove(string):
    return string.replace(" ", "")

def setAlarm(tim):
        
    # time.sleep(5)
    # x,y = pyautogui.position()
    # print(x,y)
    # pyautogui.click(195,216)
    #   
    tim = tim.split()
 
    if(len(tim[0]) ==3  ):
        h= tim[0][0:1]
        h = int(h)
        # print(int(h))
        
        m= tim[0][1:3]
        m=int(m)
        # print(int(m))
    elif(len(tim[0]) ==4 ):
        h= tim[0][0:1]
        h = int(h)
        print(int(h))
        
        m= tim[0][2:4]
        m=int(m)
        print(int(m))
    elif len(tim[0]) ==5:
        h= tim[0][0:2]
        h = int(h)
        print(int(h))
        
        m= tim[0][3:5]
        m=int(m)
        print(int(m))
        time.sleep(2)
    pyautogui.click(650, 1100) 

    time.sleep(2)

    pyautogui.press('c')
    time.sleep(1)
    pyautogui.press('l')

    pyautogui.press('o')
    time.sleep(1)

    pyautogui.press('c')
    time.sleep(1)

    pyautogui.press('k')
    time.sleep(5)

    pyautogui.click(650, 350) 

    time.sleep(13)

    for i in range(6):
        pyautogui.press('tab')
    pyautogui.press('enter')    

    time.sleep(5)
    x,y = pyautogui.position()


    print(len(tim[0]), tim[0],)



    for i in range(5):
        pyautogui.press('up') 


    for i in range(h):
        pyautogui.press('up') 


    pyautogui.press('tab') 

    for i in range (m) :
        # print(i)
        pyautogui.press('up') 

    pyautogui.press('tab')  

    if(tim[1][0]=="p"):
        pyautogui.press('up') 

    for i in range(6):
        pyautogui.press('tab') 


    pyautogui.press('enter')
    time.sleep(2) 
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    time.sleep(1)
    pyautogui.keyUp('alt')  
    speak(f"Alarm has been set at {tim}")
    # # for t in tim:
    # #     print(t)




def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    server.starttls()
    server.login('mohammed.maaz0213@gmail.com', 'ymuv nqni njyw zxll')
    server.sendmail('mohammed.maaz0213@gmail.com', to , content)
    server.close()


def pdf_reader():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() 
    # show an "Open" dialog box and return the path to the selected file
    filename=filename.replace("/" ,"\\\\")
    print(filename)

    givenFile  = filename [ filename.rindex("\\")+1 : ]

    
    shutil.copy(filename , "C:\\Users\\LENOVO 7XIN\\OneDrive\\Desktop\\ULTRON\\Mypdfs")


    book = open(f"Mypdfs/{givenFile}" , "rb")
    pdfReader =PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak("Enter the page number ")
    pg =  takeCommand()
    
    s= pg.split()
    # print(s)
    x = int (s[1]               
    )
    
    # print(x-1)

    page = pdfReader.getPage(x-1)
    text = page.extractText()
    print(text)
    speak(text)

def changeRate():
    speak("What speed do you want")
    r= takeCommand().lower()
    engine.setProperty('rate', rates[r])



def taskExecution():
    
    wish()

    while True :
    # if 1:

        query =  takeCommand().lower()

        if "open notepad"  in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif "open the notepad"  in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)


        
        elif "change rate" in query:
            changeRate()

        elif "change the rate" in query:
            changeRate()   

        elif "open command prompt" in query:
            cpath="C:\\Users\\LENOVO 7XIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(cpath)
        
        elif "open the command prompt" in query:
            cpath="C:\\Users\\LENOVO 7XIN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(cpath)


        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam' , img )
                k= cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows() 
       
       
        elif "open the camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam' , img )
                k= cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows() 
       
       
        elif "close camera" in query:
            pyautogui.press('esc')
        # elif "open camera" in query:
        
        elif "close the camera" in query:
            pyautogui.press('esc')
       
        elif "play music" in query:
            speak("What song, Sir ?")
            song  = takeCommand()
            song =  song+'.mp3'
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            song = remove(song).lower()

            for s in songs:
                if song == s:
                    os.startfile(os.path.join(music_dir,song))
                     

        elif "play some music" in query:
            speak("What song, Sir ?")
            song  = takeCommand()
            song =  song+'.mp3'
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            song = remove(song).lower()

            for s in songs:
                if song == s:
                    os.startfile(os.path.join(music_dir,song))
                     
        elif "play the music" in query:
            speak("What song, Sir ?")
            song  = takeCommand()
            song =  song+'.mp3'
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            song = remove(song).lower()

            for s in songs:
                if song == s:
                    os.startfile(os.path.join(music_dir,song))
                     

             # os.startfile(os.path.join(music_dir,songs[0]))
        elif "ip address" in query:
            ip= get("https://api.ipify.org").text
            speak(f" Your ip address is  {ip}")

        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            print(query)
            results = wikipedia.summary(query, sentences=2)
            speak("Accoring to wikipedia")
            speak(results)
            print(results)
            
        # elif "stop ultron" in query:
        #     break    

        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")    

       
        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm=  takeCommand().lower()

            webbrowser.open(f"{cm}")    

        elif "send message through whatsapp" in query:
            # speak("")     
            webbrowser.open("https://web.whatsapp.com")    
            time.sleep(15)
            speak("to who")
            user = remove(takeCommand().lower())
            
            pyautogui.click(195,216)
            for i in user:
                pyautogui.press(i)
            pyautogui.press("enter")
            time.sleep(3)
            speak("What is the message?")
            msg = takeCommand().lower()

            for i in msg:
                pyautogui.press(i)

            pyautogui.press('enter')    
            time.sleep(2)    

            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            no= remove(takeCommand())
            # no = "+91"+no
            # kit.sendwhatmsg(no, "asfasfdsfs" , 12,19    )
            

        elif "send some message through whatsapp" in query:
            # speak("")     
            webbrowser.open("https://web.whatsapp.com")    
            time.sleep(15)
            speak("to who")
            user = remove(takeCommand().lower())
            
            pyautogui.click(195,216)
            for i in user:
                pyautogui.press(i)
            pyautogui.press("enter")
            time.sleep(3)
            speak("What is the message?")
            msg = takeCommand().lower()

            for i in msg:
                pyautogui.press(i)

            pyautogui.press('enter')    
            time.sleep(2)    

            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            no= remove(takeCommand())
            # no = "+91"+no
       
        elif "play songs on youtube" in query:
            speak("Sir, which song?")
            song = takeCommand().lower()
            kit.playonyt(song)    
            time.sleep(5)


       
        elif "play some songs on youtube" in query:
            speak("Sir, which song?")
            song = takeCommand().lower()
            kit.playonyt(song)    
            time.sleep(5)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                speak("email ?")
                to = takeCommand().lower()
                to=remove(to)
                # to = "waheedbros@gmail.com"
                print(remove(to))
                print(content)
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Some error occurred")        

        elif "send an email" in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()
                speak("email ?")
                to = takeCommand().lower()
                to=remove(to)
                # to = "waheedbros@gmail.com"
                print(remove(to))
                print(content)
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Some error occurred")        


        elif "no thanks" in query: 
            speak("Thanks for using me ")
            sys.exit()   
      
        # elif "wait a minute" in query:
        #     speak("Sir, how much time")

        #     time.sleep(10)
     
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")   
        
        elif "close the notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")   
 
        # elif "set alarm" in query:
        #     speak("")
        
        elif "set alarm" in query:
            speak("Setting an alarm")
            time.sleep(1)
            speak("What time?")
            alarm = takeCommand().lower()
            setAlarm(alarm)

        elif "set an alarm" in query:
            speak("Setting an alarm")
            time.sleep(1)
            speak("What time?")
            alarm = takeCommand().lower()
            setAlarm(alarm)


        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)      
        
        elif "tell a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)      
         

        elif "switch the tab" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
        
        elif "close the tab" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            time.sleep(1)
            pyautogui.keyUp('alt')  

        elif "temperature" in query:
            res = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=17.4122998&lon=78.267959&appid=94d65bb26e67c1b54dabcec6a215fdcc&=celsius')
            response = json.loads(res.text)
            speak(f"the temperature of hyderabad is { round(response['main']['temp']-273 , 2 )}")
        
        elif "activate how to do mode" in query:
            from pywikihow import search_wikihow
            speak("How to do mode is activated, please tell me what you want to know")
            how = takeCommand()
            max_results=1
            how_to= search_wikihow(how,max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary )

        elif "read pdf" in query:
            pdf_reader()
        elif "read the pdf" in query:
            pdf_reader()  

        elif "hello" in query:
            speak("Hello sir, may I help you with something")

        elif "hey" in query:
            speak("Hello sir, may I help you with something")

        elif "how are you" in query:
            speak("I am fine sir, how about you")

        elif "also good" in query:
            speak("That's great to hear from you")


        elif "fine" in query:
            speak("That's great to hear from you")

        elif "thank you"  in query:
            speak("It's my pleasure sir")

        elif "thanks"  in query:
            speak("It's my pleasure sir") 

        elif "pause" in query: 
            speak("Ok sir, I am going to sleep. You can call me anytime")
            break
           

if __name__=="__main__":



    while True:
        permission = takeCommand()
        if "wake up" in permission:
            taskExecution()
        elif "goodbye" in permission:
            speak("Thanks for using me sir, have a good day")
            sys.exit()    