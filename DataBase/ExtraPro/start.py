import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    rr = open('D:\\ULTRON\\EDITH\\Data.txt','rt')
    query = str(rr.read())
    rr.close()
    sss = open('D:\\ULTRON\\EDITH\\Data.txt','r+')
    sss.truncate(0)
    sss.close()
    webdriver = "D:\\ULTRON\\EDITH\\DataBase\\webdriver\\chromedriver.exe"
    photos = "D:\\ULTRON\\EDITH\\DataBase\\GooglePhotos"
    search_keys = [f"{query}"]
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)
    for search_key in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

    os.startfile(photos)
