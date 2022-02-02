import pyperclip
import pywhatkit
import wikipedia
from pywikihow import WikiHow,search_wikihow
import os
import pyttsx3
import webbrowser
from pytube import YouTube
from pyautogui import click,hotkey
from pyperclip import paste
from time import sleep
import speedtest
import wolframalpha
import requests
import pyautogui as pa

searchbar = pa.locateCenterOnScreen('D:\\ULTRON\\EDITH\\DataBase\\PyAutoGui\\Youtube\\SearchBar.png')
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-2].id)
    engine.setProperty('rate',170)
    print("  ")
    print(f": {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

def GoogleSearch(term):
    query = term.replace("edith","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace("google search","")
    query = query.replace("Google Search","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab  = str(query)
    rrr = open('D:\\ULTRON\\EDITH\\Data.txt','a')
    rrr.write(writeab)
    rrr.close()
    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)
        
    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query,2)
        speak(f": As per you command i Found this : {search}")

def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    speak("This is found on the Web Boss")
    pywhatkit.playonyt(term)
    speak("This May help you Boss")

def Alarm(query):
    TIME = open('D:\\ULTRON\\EDITH\\Data.txt','a')
    TIME.write(query)
    os.startfile("D:\\ULTRON\\EDITH\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube():

    sleep(2)
    click(x=497,y=47)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):
        url = YouTube(link)
        video = url.streams.get_highest_resolution()

        video.download('D:\\ULTRON\\EDITH\\DataBase\\YoutubeVideo')


    Download(Link)


    speak("Done Sir , I Have Downloaded The Video .")

    speak("You Can Go And Check It Out.")
    os.startfile('D:\\ULTRON\\EDITH\\DataBase\\YoutubeVideo')

def InternetSpeed():
        speak("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        speak(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

def Wopha(query):
    key = open('D:\\ULTRON\\EDITH\\DataBase\\API KEYS\\wolfalpha.cp','rt')
    API = key.readline()
    key.close()
    Api_Key = API
    request = wolframalpha.Client(Api_Key)
    requested = request.query(query)
    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("An String Value Is Not Answerable")

def Calculator(query):
    Term = str(query)
    Term = Term.replace("edith","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","*")
    Term = Term.replace("into","*")
    final = str(Term)
    try:
        result = Wopha(final)
        speak(f"your answer is {result}")
    except:
        speak("I can't find any answer")

def Temp(query):
    Term = str(query)
    Term = Term.replace("edith","")
    Term = Term.replace("in","")
    Term = Term.replace("what is the","")
    Term = Term.replace("tempreture","")
    temp = str(Term)
    if 'outside' in temp:
        var1 = "Tempreatur in indore"
        answer = Wopha(var1)
        speak(f"Boss Tempreature outside in indore is {answer}")
    else:
        var2 = "Tempreature In" + temp
        anw = Wopha(var2)
        speak(f"Boss the Tempreture is {anw}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def YoutubeAudio():
    sleep(2)
    pa.moveTo(searchbar)
    pa.click()
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)
    youtube_link = Link
    y = YouTube(youtube_link)
    t = y.streams.filter(only_audio=True).all()
    t[0].download(output_path="D:\\ULTRON\\EDITH\\DataBase\\YoutubeAudio")