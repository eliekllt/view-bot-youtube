import selenium
from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title YOUTUBE VIEWBOT')

print(pyfiglet.figlet_format("BOT YOUTUBE GHOSTMAN", font="slant"))
print("!You must accept cookies the first time and launch the video!")

vidUrl = input("Link of the video: ")
tps = int(input("How long should the bots stay on the video (suggestion : 20s) : "))
nb = int(input("How many views do you want : "))

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome( options=chrome_options)
driver.set_window_size(500,500)
i=1
for i in range(nb):
        driver.get(vidUrl)
        sleep(tps)
        driver.refresh()
        print("Number of views added : ",i)
driver.close()
print("Adding views completed.")
print("Press enter to exit")
input()
exit()