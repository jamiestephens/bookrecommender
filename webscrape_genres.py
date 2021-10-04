# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 04:45:12 2021

@author: Administrator
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 02:48:50 2021

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import csv 
import numpy as np

def newgenrepage(driver,allgen_arr):
    elems = driver.find_elements_by_xpath("//*[@class='shelfStat']")
    for elem in elems:
            split_text = elem.text.split()
            genrename = (split_text[0].replace("'",""))
            linktext = (elem.find_element_by_css_selector('a').get_attribute('href').replace("'",""))
            bookcount = split_text[1].strip("'")
            bookcount = bookcount.replace(',','')
            allgen_arr = np.append(allgen_arr, [[genrename,bookcount,linktext]],axis = 0) 
    try:
        driver.find_element_by_partial_link_text("next »").click()
        newgenrepage(driver,allgen_arr)
    except NoSuchElementException:
        writetocsv(allgen_arr)


def writetocsv(allgen_arr):
    csv_name = "./data/genres.csv"
    
    try:
        with open(csv_name, 'w+', encoding="utf-8") as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(allgen_arr)
    except IOError:
        print("I/O error")
    
        
if __name__ == "__main__":
    URL = 'https://www.goodreads.com/genres/list?page=1'
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    time.sleep(30)
    driver.refresh()
    driver.refresh()
    allgen_arr = np.array([['Genre Name','Count','Link']]) 
    newgenrepage(driver,allgen_arr)