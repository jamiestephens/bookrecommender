# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:35:53 2021

@author: Jamie Stephens
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import NoSuchElementException
import time
from sqlalchemy import create_engine

def traversegenrelist():
    URL = 'https://www.goodreads.com/genres/list'
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\AppData\Local\Programs\Python\geckodriver\geckodriver.exe')
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    time.sleep(30)
    driver.refresh()
    print("First refresh")
    driver.refresh()
    print("Second refresh")
    elems = driver.find_elements_by_xpath("//*[@class='shelfStat']")
    genrearray = []
    arrayofarrays = []
    i = 0
    for elem in elems:
        if i < 1:
            split_text = elem.text.split()
            textname = split_text[0]
            linktext = elem.find_element_by_css_selector('a').get_attribute('href')
            booktotal = split_text[1]
            print("Genre name: ",textname)
            print("Link: ",linktext)
            print("Book total: ",booktotal)
            genrearray.extend([textname, linktext, booktotal])
            arrayofarrays.append(genrearray)
            gotogenrepage(linktext,driver)
            i = i + 1
            print("i is: ",i)

def gotogenrepage(linkt,driver):
    driver.execute_script("window.open('" + linkt +"');")
    wait = WebDriverWait(driver, 10)
    try:
        morelink = driver.find_element_by_xpath("//*[@class='moreLink']")
        morelinktext = morelink.find_element_by_css_selector('a').get_attribute('href')
    except NoSuchElementException:
        print("False")
    print("true")
    driver.close()
    
    
if __name__ == "__main__":
    traversegenrelist()