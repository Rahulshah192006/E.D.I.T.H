import requests
import os
from PIL import Image
import pyttsx3
import random

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

def MarsImage():
    name = 'curiosity'
    date = input('Enter Date For extracting of data:-')
    Api_ = str(api_key)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"
    r = requests.get(url)
    data = r.json()
    Photos = data['photos'][:20]
    try:
        for index,photo in enumerate(Photos):
            Camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = Camera['name']
            full_camera_name = Camera['full_name']
            date_of_photo = photo['earth_date']
            imaage_url = photo['img_src']
            pro = requests.get(imaage_url)
            img = f'{index}.jpg'
            with open(img,'wb') as file:
                file.write(pro.content)
            path_1 = "D:\\ULTRON\\EDITH\\" + str(img)
            path_2 = "D:\\ULTRON\\EDITH\\DataBase\\Nasa\\MarsImages\\" + str(img)
            os.rename(path_1,path_2)
            os.startfile(path_2)
        speak(f"This Image Was Captured With : {full_camera_name}")
        speak(f"This Image Was Captured On : {date_of_photo}")

    except:
        speak("Something Went wrong")
MarsImage()

