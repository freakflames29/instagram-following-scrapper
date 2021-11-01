import time
import os
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

USERNAME = 'YOUR USER NAME'
PASSWORD = "YOUR PASSWORD"
try:

    def mainFun(user):
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        usnmae = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passw = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        usnmae.send_keys(USERNAME)
        passw.send_keys(PASSWORD)
        passw.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get('https://www.instagram.com/{user}/'.format(user=user))

        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        print("Searching the following ...")
        time.sleep(3)
        for i in range(0, 100):
            driver.execute_script("document.querySelector('.isgrP').scrollTo(0,{y})".format(y=i * 500))
            time.sleep(3)
        names = driver.find_elements_by_class_name('FPmhX')
        print("Gotcha Follwers scraped " + str(len(names)) + " ! writting followers in followers.txt...")

        os.system('notify-send "Printing follwings..." && paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
        
        er = open('follwers.txt', 'r+')
        er.truncate()
        er.close()
        with open("follwers.txt", 'at') as f:

            f.write("Total Followers scraped: {count} \n".format(count=len(names)))
            for name in names:
                wr = name.text + " --> " + name.get_attribute('href')
                f.write(wr + '\n')
                print(wr)
            f.close()
        print("Done " + str(len(names)) + " following found !Check followers.txt")
except:
    print("error")

user = input("Enter the username you want to search :- ")
print("Visiting {name} profile on instagram".format(name=user))
mainFun(user)
