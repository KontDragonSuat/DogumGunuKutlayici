# -*- coding: utf-8 -*-

from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from hesap import account, password

def zamangeldi():
    def wait():
        driver.implicitly_wait(20)
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--incognito")
    chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver = webdriver.Chrome()
    driver.get("https://instagram.com/login")
    driver.implicitly_wait(60)
    driver.delete_all_cookies()
    driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input").send_keys(account)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    try:
        hata = driver.find_element(By.ID, "slfErrorAlert")
        if hata.is_enabled():
            print("Giriş Yapılamadı!")
            exit()
    except:
        print()
    driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Direct']").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "div[class='_abm0']").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "input[name='queryBox']").send_keys(kime)
    wait()
    driver.find_element(By.CSS_SELECTOR, "circle[cy='12']").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "div[class='_aagz']").click()
    wait()
    driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(dgkomsj)
    wait()
    driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(Keys.ENTER)

def calistir():
    try:
        zamangeldi()
        print("Mesaj gönderildi")
    except:
        print("Bir hata ile karsilasildi!")

while True:
    sleep(86400)
    zaman = datetime.now()
    if zaman.month == 2 and zaman.day == 26:
        kime = "c3lebi.blknl1"
        dgkomsj = "Dogum gunun kutlu olsun gardasim"
        calistir()
