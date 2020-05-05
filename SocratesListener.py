#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:47:21 2020

@author: elliott
"""
import speech_recognition as sr
import concurrent.futures
#--------------------------------------LISTENER---------------------------------

def checkQueue(q):
    print('Checking the queue for a stop signal')
    try:
        q_is = q.get(False)
        if q_is =='stop':
            print('The queue recieved the stopper')
            return True
    except:
        print('Q is empty')
        return False

def listen(q=False):#Google
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 100
    with sr.Microphone() as source:
        print('I''m listening... \n')
        
        if q is not None and checkQueue(q)==True:#check queue for stop signal 
            return 'stop' 

        try:
            audio = r.listen(source,timeout= 5.0,phrase_time_limit=3.0)
            print('Processing audio')
        except sr.WaitTimeoutError:
            return listener(q)

    try:
        text = r.recognize_google(audio)
        print("Got it: " + text)    
        if text is None:
            print('I didn\'t hear anything.')
            return listener(q)
        else: 
            print('Returning text from listener')
            return text
        
    except sr.UnknownValueError:   
        if checkQueue(q)==True:#check queue for stop signal 
            return 'stop'         
        print("Sorry, I didn't get that")
        return listener(q)
    
    except sr.RequestError:
        print("Could not request results from Google service; {0}")
        return


def listener(q=False):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(listen,q)
        return future.result()
