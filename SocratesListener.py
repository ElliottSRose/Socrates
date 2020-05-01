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

# listen()

##class Listener():GOOGLE OOP VERSION
#    def __init__(self):    
#        self.thread = None
#        self.listenerQueue = Queue()
#        
#    def startListening(self):
#        self.thread = threading.Thread(target=self.listen, daemon=True)
#        self.thread.start()
#        
#    def stopListening(self):
#        try:
#            ('checking q.get',q)
#            if q.get(False)=='stop':
#                return True
#        except:
#            pass
#        
#    def listen(self):#GOOGLE
#        listenerQueue = Queue()
#        if self.stopListening()==True:
#            print('Okay I''ll stop listening')
#            return 
#        r = sr.Recognizer()
##        r.operation_timeout = 5
#        with sr.Microphone() as source:
#            print('I''m listening \n')
#            audio = r.listen(source)
#            print('Processing audio')
#        try:
#            text = r.recognize_google(audio)
#            print("Got it: " + text)
#            if text is None:
#                print('I didn\'t hear anything.')
#                return
#            else: 
#                print('putting text in queue')
#                return self.listenerQueue.put(text)
#        except sr.UnknownValueError:
#            print("Sorry, I didn't get that")
#            return
#        except sr.RequestError:
#            print("Could not request results from Google service; {0}")
#            print('Perhaps your internet is not connected')
#            return
#            

#def listener():
#l = Listener()
#l.startListening()
#    return l.listenerQueue.get()






#--------------------- Extra Scratch Code - IBM listener
#q.put('stop')

#def listen():#IBM
#    r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print('I''m listening... \n')
#        audio = r.listen(source)
#        print('Processing audio')
#    try:
#        text = r.recognize_ibm(audio_data=audio, )
#        print("Got it: " + text)
#     
#        if text is None:
#            print('I didn\'t hear anything.')
#            return listener()
#        else: 
#            return text
#    except sr.UnknownValueError:
#        print("Sorry, I didn't get that")
#        return listener()
#    except sr.RequestError:
#        print("Could not request results from Google service; {0}")
#
#def run():
#    with concurrent.futures.ThreadPoolExecutor() as executor:
#        future = executor.submit(listen)
#        return_value = future.result()
#        return return_value
#    print ('return_value =', return_value)
#        
        
#import threading        
#def listener(queue):
#    thread = threading.Thread(target=listen) # Always put a comma after the arguments. Even if you have only one arg.
#    thread.start() # Start the thread
#    return thread
