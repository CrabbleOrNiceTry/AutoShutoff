from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import random
import re
import time
import sys

def main():
    seconds = int (sys.argv[1]) * 60
    options = ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/NiceTry/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Chrome(executable_path="C:/Users/NiceTry/Desktop/prgTHINGS/PythonThings/_ChromeWebDriver/chromedriver.exe", chrome_options=options)
    driver.get("https://google.com")
    time.sleep(seconds)
    driver.close()
main()