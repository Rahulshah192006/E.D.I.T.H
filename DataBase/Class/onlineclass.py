
import selenium
from selenium import webdriver
import time
import datetime
from datetime import date
from selenium.webdriver.chrome.options import Options
import pyttsx3
opt = Options()
opt.add_experimental_option("prefs", { "profile.default_content_setting_values.media_stream_mic":2, 
    "profile.default_content_setting_values.media_stream_camera":2})  
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

def teams():
    emailid="email"
    password="pass"
    day1=["Hindi","Chemistry","Physics","Mathematics","Group 2 Activity ( Performing art)"]
    day2=["Hindi","Mathematics","sports","Social science","English"]
    day3=["English","Computer","Social science","Biology","Mathematics"]
    day4=["Hindi","Chemistry","Physics","Mathematics","Group 2 Activity ( Performing art)"]
    day5=["Hindi","Mathematics","library","Social science","English"]
    day6=["English","Computer","Social science","Biology","Mathematics"]
    startclass=["09:00","09:52","10:50","11:32","12:20",]
    endclass=["09:50","10:35","11:30","12:20","13:10",]
    noc=5 
    op= "D:\\ULTRON\\Teams Bot\\chromedriver.exe"
    driver = webdriver.Chrome(options=opt,executable_path=op)
    driver.get("http://teams.microsoft.com")
    time.sleep(15)
    email = driver.find_element_by_xpath('//*[@id="i0116"]')
    email.send_keys(emailid)
    speak("Boss I have entered your email id")
    time.sleep(2)
    enter=driver.find_element_by_id("idSIButton9")
    time.sleep(2)
    enter.click()
    time.sleep(2)
    passwd=driver.find_element_by_id("i0118")
    passwd.send_keys(password)
    speak("PASSWORD entered Boss")
    passbtn=driver.find_element_by_id("idSIButton9")
    passbtn.click()
    time.sleep(2)
    confirmbtn=driver.find_element_by_id("idSIButton9")
    confirmbtn.click()
    speak("I have Logged In to your Account. Loading TEAMS web app...")
    time.sleep(30)
    speak("TEAMS web app loaded")
    time.sleep(1)
    try:
        teambtn=driver.find_elements_by_css_selector('div.team-card')
        teambtn[0].click()
    except:
        j=0
        while j<=1:
            teambtn=driver.find_elements_by_css_selector('div.team-card')
            if teambtn==None:
                time.sleep(2)
                continue
            elif teambtn !=None:
                teambtn[0].click()
                speak(" successfully entered inside your team.")
                break
    time.sleep(3)
    def classjoin(x,i,y):
        speak("Boss Searching the subject channel")
        z=x[i]
        channelbtn=driver.find_element_by_xpath("//a[@title=\'"+z+"\']")
        channelbtn.click()
        speak("Channel Found")
        time.sleep(10)
        speak("Boss Looking for the join button")
        c=0
        while c<=1:
            speak("Boss is trying to join the meeting")
            time.sleep(2)
            joinbtn=driver.find_element_by_css_selector('button.ts-calling-join-button')
            if joinbtn==None:
                time.sleep(2)
                continue
            elif joinbtn != None:
                joinbtn.click()
                break
                
        speak("Boss i am  joining the meeting")
        d=0
        while d<=1:
            speak("Boss is trying its best to join the meeting")
            time.sleep(2)
            conbtn=driver.find_element_by_css_selector('button.ts-btn-fluent-secondary-alternate')
            if conbtn==None:
                time.sleep(2)
                continue
            elif conbtn != None:
                conbtn.click()
                time.sleep(2)
                break    
        joinbtn2=driver.find_element_by_css_selector('button.join-btn')
        joinbtn2.click()
        time.sleep(5)
        speak("Boss has joined the meeting")
        time.sleep(5)
        try:
            time.sleep(2)
            driver.find_element_by_id('callingButtons-showMoreBtn').click()
        except:
            u=0
            while u<=1:
                speak("trying to press show more button")
                showbtn=driver.find_element_by_id('callingButtons-showMoreBtn')
                if showbtn !=None:
                    driver.find_element_by_id('callingButtons-showMoreBtn').click()
                    break 
                elif showbtn == None:
                    driver.find_element_by_css_selector('div.ts-calling-screen').click()
                    continue
        try:
            driver.find_element_by_id('incoming-video-button').click()
            speak("Boss turned video off")
            speak("Boss Comb your hair and get ready for class")
        except:
            o=0
            while o<=1:
                speak('trying my best to turn off the video')
                inbtn=driver.find_element_by_id('incoming-video-button')
                if inbtn !=None:
                    driver.find_element_by_id('incoming-video-button').click()
                    break
                elif inbtn==None:
                    time.sleep(10)
                    driver.find_element_by_css_selector('div.ts-calling-screen').click()
                    driver.find_element_by_id('callingButtons-showMoreBtn').click()
                    continue
                    
        speak("Boss has turned incoming video off")
        endtime=y[i]
        m=0
        while m<=1:
            if time.strftime('%H:%M')==endtime:
                speak("Boss I am leaving the meeting")
                try:
                    driver.find_element_by_css_selector('div.ts-calling-screen').click()
                    driver.find_element_by_id('hangup-button').click()
                    speak("Boss I left the meeting")
                except:
                    y=0
                    while y<=1:
                        speak("Boss I am leaving the meeting")
                        exitbtn=driver.find_element_by_id('hangup-button')
                        if exitbtn==None:
                            driver.find_element_by_css_selector('div.ts-calling-screen').click()
                            continue
                        elif exitbtn !=None:
                            driver.find_element_by_id('hangup-button').click()
                            driver.find_element_by_id('hangup-button').click()
                            break
                                    
                speak("Boss I left the class")
                break
            else:
                continue
                
                
        
    if date.today().weekday()==0:
        speak(" Boss checking MONDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day1,x,endclass)
                    continue

    if date.today().weekday()==1:
        speak(" Boss checking TUESDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day2,x,endclass)
                    continue

    if date.today().weekday()==2:
        speak(" Boss checking WEDNESDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day3,x,endclass)
                    continue


    if date.today().weekday()==3:
        speak(" Boss checking THRUSDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day4,x,endclass)
                    continue
        

    if date.today().weekday()==4:
        speak(" Boss  checking FRIDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day5,x,endclass)
                    continue
            


    if date.today().weekday()==5:
        speak(" Boss  checking SATURDAY Timetable")
        i=0
        while i<=1:
            speak("Looking for class...")
            for x in range(0,noc):
                if time.strftime('%H:%M')==startclass[x]:
                    speak(" : Its time for the class")
                    classjoin(day6,x,endclass)
                    continue



number = 'enter your mob number'
passw = 'password'
op= "D:\\ULTRON\\Teams Bot\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=op) 

def vednatuClass():
    driver.get('https://www.vedantu.com/')
    signin = driver.find_element_by_xpath('//*[@id="login-link"]')
    signin.click()
    time.sleep(1)
    vsign = driver.find_element_by_xpath('//*[@id="login-email-phone"]/input')
    vsign.click()
    vsign.send_keys(number)
    time.sleep(2)
    next = driver.find_element_by_xpath('//*[@id="login-submit3"]')
    next.click()
    time.sleep(5)
    passord = driver.find_element_by_xpath('//*[@id="password-input-field"]')
    passord.click()
    passord.send_keys(passw)
    time.sleep(1)
    next = driver.find_element_by_xpath('//*[@id="login-submit2"]')
    next.click()
    speak("Boss checking for class")
    time.sleep(15)
    try:
        speak("Class found Boss i am joining boss")
        joinbutton = driver.find_element_by_xpath('//*[@id="latest-upc-session-banner"]/table/tr/td[3]/a')
        joinbutton.click()
        time.sleep(35)
        joinsession = driver.find_element_by_xpath('//*[@id="checkAudioAndVideo"]/div[3]')
        joinsession.click()
        print("Boss i have joined the class")
    except:
        print("Boss there is no class")
