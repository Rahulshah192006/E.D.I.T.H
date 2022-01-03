import requests
import os
from PIL import Image
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)
engine.setProperty('rate',170)


def speak(audio):
    print("  ")
    print(f": {audio}")
    print("  ")
    engine.say(audio)
    engine.runAndWait()

path = open('D:\\ULTRON\\EDITH\\DataBase\\API KEYS\\Nasa_Api.txt','rt')
api_key = path.readline()
def Nasa(Date):
    speak('Boss extracting information from Nasa Datebase')
    speak('Extraction is Done Boss I found this')
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + str(api_key)
    parameter = {'date':str(Date)}
    req = requests.get(url,params=parameter)
    Date = req.json()
    exp = Date['explanation']
    title = Date['title']
    copyright = Date['copyright']
    imageHD = Date['hdurl']
    image_r = requests.get(imageHD)
    filename = str(title) + '.jpg'
    with open(filename,'wb') as f:
        f.write(image_r.content)
    default_path = "D:\\ULTRON\\EDITH"
    main_path = "D:\\ULTRON\\EDITH\\DataBase\\Nasa\\Images"
    os.rename(default_path,main_path)
    img = Image.open(main_path)
    img.show()
    speak(f"Boss title is : {title}")
    speak(f"Boss According to Nasa : {exp}")
    speak(f"Boss the image is copyright by : {copyright}")
