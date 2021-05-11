# -*- coding: utf-8 -*-
"""

@author: Jamie Stephens
"""

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def findBook(book):
    
    
    login_form = driver.find_element_by_id('loginForm')
    URL= 'https://www.goodreads.com/book'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    elems = soup.find_all("div", class_="searchBox--large__input")

    print(elems)
    
    
if __name__ == "__main__":
    findBook('Memoirs of a Geisha')