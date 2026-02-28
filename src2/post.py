from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from wojak_getter import get_wojak
import punish

from pathlib import Path
import os
import platform


import time
import random


import undetected_chromedriver as uc

load_dotenv()

homepath = os.path.expanduser('~')

def detectOS():
    return platform.system()

def chromeProfile(os):
    match os:
        case 'Windows':
            return homepath + "\selenium-profile"
        case 'Darwin':
            return homepath + "Library/Application Support/Google/Chrome"

username = os.getenv("xUSER")
password = os.getenv("xPASS")
currOS = detectOS()

op = Options()
# op.add_argument("--headless=new")
# op.add_argument("--disable-gpu")
# op.add_argument("--disable-blink-features=AutomationControlled")
op.add_argument("--user-data-dir=/selenium-profile")

print("Test")

driver = uc.Chrome(options=op)
# driver = webdriver.Chrome(options=op)
# driver.execute_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined}))""")

def human_type(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

def cookieTest():
    driver = uc.Chrome()
    driver.get('https://x.com/')
    input("Pause")



def tweetBot(number):
    driver.get('https://x.com/home')
    time.sleep(5)

    if "login" in driver.current_url.lower():

        driver.get('https://x.com/login')
        driver.implicitly_wait(15)

        input("Pause")

        preUser = driver.find_element(By.XPATH, "//input[@type='text']")
        human_type(preUser, username)

        next = driver.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        next.click()

        driver.implicitly_wait(10)

        prePass = driver.find_element(By.XPATH, "//input[@name='password']")
        human_type(prePass, password)

        signIn = driver.find_element(By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]')
        signIn.click()

        # input("Pause")
    
    path = get_wojak(number)

    file_input = driver.find_element(By.XPATH, "//input[@type='file' and @data-testid='fileInput']")
    image_path = os.path.abspath(path)

    file_input.send_keys(image_path)
    driver.implicitly_wait(10)
    time.sleep(3)

    postIt = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
    postIt.click()

    input("Pause")

    driver.quit()


# print(detectOS())
# cookieTest()