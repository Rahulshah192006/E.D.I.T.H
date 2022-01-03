import pyautogui as pa
from time import sleep
sleep(3)
searchBar = pa.locateCenterOnScreen('BAR.png')
pa.moveTo(searchBar)
pa.click()