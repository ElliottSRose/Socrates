#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:38:38 2020

@author: elliott
"""
from bs4 import BeautifulSoup, SoupStrainer
import requests
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re
    
#---------------------------------SKILLS---------------------------------------
def getMITAnswer(sentence):
#This function uses a natural language application to answer 
#questions
    sentence.replace(' ','+')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver",options=chrome_options)
    browser.get('http://start.csail.mit.edu/answer.php?query=' + sentence)  
    iframe = browser.find_element_by_tag_name("iframe")     
    browser.switch_to.default_content()     
    browser.switch_to.frame(iframe)      
    return(browser.find_element_by_css_selector("span").text)
#    else:
#        return "MIT couldn't find anything for you..."
         
def wikiAnswer(sentence):
#This function uses wikipedia give information on a topic
    url = requests.get('https://en.wikipedia.org/wiki/' + sentence)
    data = url.text
    links = SoupStrainer('p')
    tags = BeautifulSoup(data,'lxml', parse_only=links)
    return tags.text
    
