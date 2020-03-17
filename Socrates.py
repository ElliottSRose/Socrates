#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:10:58 2020

@author: elliott
"""
#required installation of homebrew, gcc, pocketsphinx
#speechrecognition,pyaudio,portaudio, and pyttsx3

from bs4 import BeautifulSoup,SoupStrainer
import pyttsx3
import requests
import speech_recognition as sr
import threading
from playsound import playsound
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

#----------------------------SKILLS---------------------------------------
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
    print('Made it here')
    print(browser.find_element_by_css_selector("span").text)    
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

#--------------------------STRING OUTPUT ORGANIZATION-------------------------

def textSeparator(text):
    text = text.lstrip()
    text = text.split('\n')
    return text

#def toSentenceSubLists(text):
#    separatedText = []
#    for paragraph in text:
#        separatedText.append(paragraph.split('.'))
#    return separatedText

def textOrganizer(text):
#    return toSentenceSubLists(textSeparator(text))
    return textSeparator(text)

#-----------------------------QUERY NEGOTIATION----------------------------

def getAnswer(sentence):
#To format our queries, we need to parse the sentence into
#usable chunks. This function will do that with 
#regular expressions
    print('sentence in getAnswer, ', sentence)
    if sentence != None:
        toList = sentence.split(' ',1)
        triggerWord = toList[0]
        if len(sentence)>1 and triggerWord =='search':
            query = wikiAnswer(toList[1])
            return answerNavigator(textOrganizer(query))
        elif triggerWord == 'stop':
            return 
        else:
    #        speech('Ok, let me check')
            answer = getMITAnswer(sentence)
            return answerNavigator(textOrganizer(answer))
    else:
        return
        
def answerNavigator(text):
#This function should take commands to move forward, backwards, and stop
#the speech engine
    
    paragraph_Number = 1 #declare the variable
    while paragraph_Number < len(text):
        
        print(str(text[paragraph_Number]), '*******paragraph number', paragraph_Number)
        speaker(str(text[paragraph_Number]))
        command = input('\n\n\n\nHit ENTER to proceed, or enter a command.\nCommand: ')
#        command = listener()
        if  command =='skip' or command == '':
            paragraph_Number+=1
            
        elif command =='back a paragraph':
            print('********* Attempting to reverse \n')
            print('******** Reading paragraph ',paragraph_Number )
            if (paragraph_Number) >= 2:
                paragraph_Number-=1
            else:
                print('This is the first paragraph...')
            
#        elif command[0] == 'search':
#            searchItem = command.split(' ',1)
#            firstIndex = command.find(searchItem)
#            command[firstIndex:firstIndex+len(searchItem)]
        elif command =='stop':
            return print("stopped reading this answer")
    return 
   
#=============================----------SPEAKER-------------=============================
            
def speak(text,engine):
    engine.say(text, 'Answer')
    try:
        engine.startLoop()
    except Exception:
        pass #handle nonsensical exception thrown ('nextfire'attribute error)

def onEnd(name, completed):
   print ('finishing', completed)
#   return completed

def speaker(query):
    engine = pyttsx3.init()
    engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel')
#    engine.connect('finished-utterance', onEnd)
    thread = threading.Thread(target=speak, args=(query,engine,)) # Always put a comma after the arguments. Even if you have only one arg.
    thread.start() # Start the thread
    while True:
#        interrupt = listener()
        interrupt = input('Stop speaker/ Continue after speaker completes. ')
        if interrupt == '':
            engine.stop()
            engine.endLoop
            thread.join()
            del engine
            break
        
#--------------------------------------LISTENER---------------------------------

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Hello sir, what can I do for you? \n')
#        speaker('Hello sir, what can I do for you?')
        audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Got it: " + r.recognize_google(audio))
        text = r.recognize_google(audio)
        if text is None:
            print('I didn\'t hear anything.')
        else: 
            return text
    except sr.UnknownValueError:
        print("Sorry, I didn't get that")
        
    except sr.RequestError as e:
        print("Could not request results from Google service; {0}".format(e))


#---------------------------------START YOUR ENGINES---------------------------
def startSocrates():
    playsound('Hello.mp3')
    query = listener()
    getAnswer(query)

#def listen():
#    listeningThread = threading.Thread(target=startSocrates,) # Always put a comma after the arguments. Even if you have only one arg.
#    listeningThread.start()


#----------------------------------TESTING-------------------------------------

def getMITAnswer_tests():
    print('\n\n\n1---------getMITAnswer(...NLP...): ',getMITAnswer('What is natural language processing?'))
    print('\n\n\n2---------getMITAnswer(...ROM...): ',getMITAnswer('What is ROM?'))
    print('\n\n\n3---------getMITAnswer(...327*454...): ',getMITAnswer('what is three hundred and twenty seven times four hundred and fifty four?'))
    print('\n\n\n4---------getMITAnswer(How is an atom split?): ',getMITAnswer('How is an atom split?'))
    print('\n\n\n5---------getMITAnswer(How does recursion work?): ',getMITAnswer('How does recursion work?'))



def answerNavigator_tests():
    print( 'answerNavigator(getAnswer(search grand canyon)', answerNavigator(getAnswer('search grand canyon')))

#speech("hello")
#speech(wikiAnswer('China'))
#print('Using Answer keyword',getAnswer('Answer What is Object Oriented Programming?'))
#print('Using Search keyword',getAnswer('Search Object Oriented Programming?'))
#speech('So now you can transcribe voice to text, make your computer speak and the world is your oyster, sick. Now we can decide how we wanna use the input. For an offhand easy idea my first instinct was to use it to open applications.')


#------------------ATTEMPTING SPEECH WITH GOOGLE TEXT TO SPEECH
#----------GTTS HAD NICER SPEECH BUT IT IS MUCH SLOWER THAN PYTTSX3
#from gtts import gTTS
#import os
##from tempfile import TemporaryFile        
#def speech(text):
#    tts = gTTS(text=text, lang='en')
#    tts.save('temp.mp3')
#    playsound('temp.mp3')
#    os.remove('temp.mp3')
#    
#
#--------------------------POCKET-SPHINX SPEECH RECOGNITION
#def startSocrates():
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print('Hello sir, what can I do for you?')
#        audio = r.listen(source)
#        text = r.recognize_sphinx(audio)
#    # recognize speech using Sphinx
#    try:
#        print("I think you said " + text)
#        getAnswer(text)
#    except sr.UnknownValueError:
#        print("Sorry sir, I could not understand audio")
##        speech("Sorry sir, I could not understand audio")
#    except sr.RequestError as e:
#        print("Sphinx error; {0}".format(e))
#
#
#getMITAnswer_tests()
#answerNavigator_tests()
startSocrates()