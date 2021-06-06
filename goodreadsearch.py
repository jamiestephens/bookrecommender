# -*- coding: utf-8 -*-
"""

@author: Jamie Stephens
"""

import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains

def findBook(book):
    URL= 'https://www.goodreads.com/book'
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    el = wait.until(EC.visibility_of_element_located((By.ID, "explore_search_query")))
    el.send_keys(book)
    el.send_keys(Keys.ENTER)
    time.sleep(15)
    driver.refresh()
    
    if EC.visibility_of_element_located((By.ID, "modal__content")):        
        print("yes")
        
    #book = driver.find_element_by_css_selector('button.gr-iconButton')
    #print(book)
    
    print("Book found is: ",driver)
    print("Author: ")
    answer = (input("Continue? (Y/N): "))
    if str(answer) == "Y":
        #idbooktypes(link)
        pass
   
def idbooktypes(link):
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
    driver.maximize_window()
    driver.get(link)
    genres = []
    for elm in driver.find_elements_by_class_name("elementList"):
        genres.append(elm.text)
        
    genres1 = []
    for i in genres:
        j = i.split('\n', 1)
        jk = j[0]
        genres1.append(jk)
    
    l = 0
    for m in genres1:
        l = l + 1
        print(l," ",m)
    genres2 = []
    
    answer = 0
    while answer != 'N':
        answer = input("Select the corresponding number of each genre to use in recommendation, or N to continue: ")
        if answer.isdigit() and answer in range(1,l):
            print("Yes")
            genres2.append(genres1[int(answer)])
    else:
        print(genres2)

    
    #print(genres2)
    
    answer1 = (input("Select 1 for faster search or 2 for an in-depth search: "))
    
def quicksearch():
    pass


def indepthsearch():
    pass
    
if __name__ == "__main__":
    findBook('Memoirs of a Geisha')
    #idbooktypes('https://www.goodreads.com/book/show/929.Memoirs_of_a_Geisha?from_search=true&from_srp=true&rank=1')