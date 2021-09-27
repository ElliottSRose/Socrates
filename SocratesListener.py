#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:47:21 2020

@author: elliott
"""
import speech_recognition as sr
import concurrent.futures
from pocketsphinx import Pocketsphinx
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

def listen(use_sphinx=False, q=False):#Google
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.energy_threshold = 100
    with sr.Microphone() as source:
        print('I''m listening... \n')

        if q is not None and checkQueue(q)==True:#check queue for stop signal
            return 'stop'

        try:
            audio = r.listen(source,timeout= 4.0,phrase_time_limit=3.0)
            print('Processing audio')
        except sr.WaitTimeoutError:
            return listener(use_sphinx,q=q)

    try:
        if use_sphinx==True:
        #     print('USING SPHINX')
        #     text = r.recognize_sphinx(audio, language = "en-US", show_all = False)
        #     print("Got it, sphinx heard: " + text)
        # else:
            print('USING GOOGLE')
            text = r.recognize_google(audio)
            print("Got it, google heard: " + text)
        if text is None:
            print('I didn\'t hear anything.')
            return listener(use_sphinx,q=q)
        else:
            print('Returning text from listener. use_sphinx is', use_sphinx )
            return text

    except sr.UnknownValueError:
        if checkQueue(q)==True:#check queue for stop signal
            return 'stop'
        print("Sorry, I didn't get that")
        return listener(use_sphinx,q)

    except sr.RequestError:
        print("Could not request results from Google service; {0}")
        return


def listener(use_sphinx=False,q=False):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(listen,use_sphinx,q)
        return future.result()


# def callback(recognizer, audio):
#     try:
#         text = r.recognize_sphinx(audio, language = "en-US", keyword_entries= [('hello')],show_all = False)
#         print("Got it: " + text)
#         if text is None:
#             print('I didn\'t hear anything.')
#             return listen_background(q)
#         else:
#             print('Returning text from listener')
#             if text == 'hello':
#                 return "it worked"
#             else:
#                 return listen_background(q)

#     except sr.UnknownValueError:
#         # if checkQueue(q)==True:#check queue for stop signal
#             # return 'stop'
#         print("Sorry, I didn't get that")
#         return listen_background(q)

#     except sr.RequestError:
#         print("Could not request results from Google service; {0}")
#         return "closing"



# def listen_background(q=False):#Google
#     r = sr.Recognizer()
#     r.dynamic_energy_threshold = False
#     r.energy_threshold = 100
#     with sr.Microphone() as source:
#         print('I''m listening... \n')

#         # if q is not None and checkQueue(q)==True:#check queue for stop signal
#         #     return 'stop'

#         try:
#             audio = r.listen_in_background(source, callback)
#             print('Processing audio')
#         except sr.WaitTimeoutError:
#             return listen_background(q)
# from queue import Queue
# q = Queue()
# listen(True, q)

# listen_background(q)
