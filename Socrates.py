#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:10:58 2020

@author: elliott
"""
#required installation of homebrew, gcc, pocketsphinx
#speechrecognition,pyaudio,portaudio, and pyttsx3

from SocratesSkills import *
from SocratesListener import *
from SocratesSpeech import *

#---------------------------------START YOUR ENGINES--------------------------

def startSocrates(q=False):
    if q is not None:
        q.queue.clear() #if Socarates is ran withouth the UI, this keeps the queue clear
    playsound('hello.mp3')
    while True:
        query = listener(q)
        if query=='stop':
            print("Stopping Socrates.")
            return
        elif query is not None:
            answer = getAnswer(q,query)
            print('Answer from getAnswer =',answer)
            if answer== False or answer==None:
                playsound('TryAgain.mp3')
                print('Keep trying with those commands, chief')
            elif answer=='stop':
                print('Stopping Socrates')
                return 
    
# startSocrates()
#----------------------------------TESTING-------------------------------------

def getMITAnswer_tests():
    print('\n\n\n1---------getMITAnswer(...NLP...): ',getMITAnswer('What is natural language processing?'))
    print('\n\n\n2---------getMITAnswer(...ROM...): ',getMITAnswer('What is ROM?'))
    print('\n\n\n3---------getMITAnswer(...327*454...): ',getMITAnswer('what is three hundred and twenty seven times four hundred and fifty four?'))
    print('\n\n\n4---------getMITAnswer(How is an atom split?): ',getMITAnswer('How is an atom split?'))
    print('\n\n\n5---------getMITAnswer(How does recursion work?): ',getMITAnswer('How does recursion work?'))

def answerNavigator_tests():
    print( 'answerNavigator(getAnswer(search grand canyon)', answerNavigator(getAnswer('search grand canyon')))
    print( 'answerNavigator(getAnswer(search quantum computing', answerNavigator(getAnswer('search quantum computing')))

def wikiAnswer_tests():
    print('wikiAnswer tests-- China',wikiAnswer('China'))

def getAnswer_tests():
    print('Using Answer keyword',getAnswer('Answer What is Object Oriented Programming?'))
    print('Using Search keyword',getAnswer('Search Object Oriented Programming?'))

def speaker_tests():
    speaker("hello")
    speaker(wikiAnswer('China'))
    speaker('So now you can transcribe voice to text, make your computer speak and the world is your oyster, sick. Now we can decide how we wanna use the input. For an offhand easy idea my first instinct was to use it to open applications.')

#getMITAnswer_tests()
#answerNavigator_tests()
#startSocrates()