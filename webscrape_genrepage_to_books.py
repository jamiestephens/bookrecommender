# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:52:02 2021

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import csv 
import numpy as np


def genrepage():
    i = 0 
    file = open('./data/genres.csv', newline='',)
    csv_reader = csv.reader(file)    
    next(csv_reader)    
    for row in csv_reader:
        URL = row[2]
        print(URL)
        driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
        driver.maximize_window()
        driver.get(URL)
        if i < 1:
            time.sleep(30)
            driver.refresh()
            driver.refresh()
        genredescription = driver.find_element_by_xpath("//*[starts-with(@id, 'freeText')]").text
        print(genredescription)
        i = i + 1
    
    
    # with open('./data/genres.csv', newline='') as csvfile:
    #      for row in csvfile:
            
    #         URL = row.split(',')[2]
    #         print("Genre number: ",i)
    #         print(URL)
    #         i = i + 1
    #         driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
    #         driver.maximize_window()
    #         driver.get(URL)
    #         if i < 1:
    #             time.sleep(30)
    #             driver.refresh()
    #             driver.refresh()
    #         genredescription =  driver.find_element_by_id("freeText*")
            
    
    





if __name__ == "__main__":
    genrepage()