import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(r'chromedriver')

def login():
    email = ''
    password = ''

    driver.get('https://www.galabingo.com') #open site
    time.sleep(5)

    pyautogui.press('F11') # make full screen
    time.sleep(5)

    pyautogui.moveTo(1525,1040,duration=0.5) # accept cookies
    pyautogui.click()
    time.sleep(3.7)

    login = driver.find_element(By.XPATH, '/html/body/vn-app/vn-dynamic-layout-single-slot[2]/vn-header/header/nav/vn-header-section[2]/vn-h-button[2]/vn-menu-item/a')
    login.click() # login button
    time.sleep(3.5)

    #login
    pyautogui.write(email, interval=0.25)
    pyautogui.press('tab')
    pyautogui.write(password,interval=0.25)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(7)

def prosecco():
    fav = []
    fav1 = (200,1000)
    pyautogui.moveTo(fav1,duration=0.4) # favourite button
    pyautogui.click()
    time.sleep(2.5)

    prosecco = pyautogui.moveTo(400,900,duration=0.2) #prosseco room
    pyautogui.click()
    time.sleep(20)
    pop_up = pyautogui.moveTo(220,125,duration=0.6) #bingo room menu
    pyautogui.click()


def free_bingo():
    time.sleep(600)
    driver.close()
    

login()
prosecco()
free_bingo()
