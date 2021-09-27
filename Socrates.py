#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:10:58 2020

@author: elliott
"""
#required installation of homebrew, gcc
#speechrecognition,pyaudio,portaudio, and pyttsx3

from SocratesSkills import *
from SocratesListener import *
from SocratesSpeech import *

#---------------------------------START YOUR ENGINES--------------------------

def startSocrates(q=False):
    while True:
        query = listener(True, q)
        if query == 'socrates':
            return internalstartSocrates(q)
        if query == 'exit':
            return 'closing program'
        else:
            return startSocrates(q)

def internalstartSocrates(q):
    s = createSpeaker()
    if q is not None:
        q.queue.clear() #if Socarates is ran withouth the UI, this keeps the queue clear
    playsound('Yes.mp3')
    while True:
        query = listener(q=q)
        print('this query was recieved at the first listener')
        if query=='stop':
            s.stop()
            print("Stopping Socrates.")
            return startSocrates(q)

        elif query is not None:
            answer = getAnswer(q,query)
            print('Answer from getAnswer =',answer)

            if answer== False or answer==None:
                print('Keep trying with those commands')

            elif answer=='stop':
                s.stop()
                print('Stopping Socrates')
                return startSocrates(q)

            else:#need to add if statement to deal with 'find' command
                s.speaker(answer)
                while True:
                    print('WL running from last while loop')
                    command = listener(q=q)
                    command = command.split(' ',1)
                    print('WL listener returned command', command)
                    if command[0]=='stop':
                        s.stop()
                        print('WL stopper fired before Socrates restart')
                        return startSocrates(q)
                    elif command[0] =='find':
                        newAnswer = answerNavigator(q,s,command,answer)
                        print('WL trying to speak, command is: ',command)
                        s.speaker(newAnswer)


# from queue import Queue
# que = Queue()
# startSocrates(que)
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
# startSocrates()
