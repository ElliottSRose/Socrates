#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:00:05 2020

@author: elliott
"""
from os import walk
import pyttsx3
import threading
from playsound import playsound
import re
from SocratesSkills import*
from SocratesListener import *
from SocratesSpeaker import *

#--------------------------STRING OUTPUT ORGANIZATION-------------------------
def textSeparator(text):
    text = text.lstrip()
    text = text.split('\n')
    return text

def textOrganizer(text):
#    return toSentenceSubLists(textSeparator(text))
    return textSeparator(text)

#-----------------------------QUERY NEGOTIATION--------------------------------
def findFile(triggerWord): 
    print(triggerWord)
    folder = []
    for (dirpath, dirnames, filenames) in walk('.'):
        folder.extend(filenames)
        break
    result = [files for files in folder if triggerWord.lower() in files.lower()] 
    print('I\'ve found these files:', result)
    choice = input('Which index would you like? ')
    return result[int(choice)]

def openFile(triggerWord):
    path = findFile(triggerWord)
    with open(path, 'r') as file:
        text = file.read().strip('\n[0-9]')
        file.close()
        return text
        
def getAnswer(q,sentence):
#To format our queries, we need to parse the sentence into
#usable chunks. This function will do that with 
#regular expressions
    if len(sentence)>1:
        toList = sentence.split(' ',1)
        triggerWord = toList[0]
        
        if len(sentence)>1 and triggerWord =='search':
            playsound('okSearch.mp3')
            query = wikiAnswer(toList[1])
            return answerNavigator(q,query)
        
        elif triggerWord == 'open':
            playsound('okOpen.mp3')
            query = openFile(toList[1])
            return answerNavigator(q,query)
        
        # else:
        #     playsound('okMIT.mp3')
        #     answer = getMITAnswer(sentence)
        #     return answerNavigator(answer)
    elif sentence=='stop':
        return 'stop'
    return False
    
def createSpeaker():
    return Speaker()   
    
def answerNavigator(q,text):
#This function should take command to find a keyword and then read from that sentence on
    text = str(text)
    print(text)
    
    s = createSpeaker()
    s.speaker(text)
    
    command = listener(q)
    command = command.split(' ',1)
    
    if command[0] == 'find':
        s.stop() 
        playsound('letMeCheck.mp3')
        firstIndex = re.search(r'[^?.]*'+ command[1],text)
        if firstIndex!=None:
            print('FOUNDTEXT:',(text[firstIndex.start():]))
            return answerNavigator(q,text[firstIndex.start():])
        else: 
            print('I couldn\'t find that')
            return answerNavigator(q,text)
        
    elif command[0] =='stop':
        s.stop()
        playsound('stop.mp3')
        print("Okay, I'll shut up")
        q.put('stop')
        return 'stop'
    else:
        print('Sorry, I\'m not programmed for that command yet.')
        return False


#=============================----------SPEAKER-------------===================       
def createSavedSpeechFiles(text):
    from gtts import gTTS
    tts = gTTS(text=text, lang='en')
    filename = input('Filename= ')
    tts.save(filename)


#def speak(text,engine):
#    def onEnd(name, completed):
#       print ('finishing', name, completed)
#       engine.stop()
#       engine.endLoop()
#       thread.join()
#    engine.connect('finished-utterance', onEnd)
#    engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel')
#    engine.say(text, 'Answer')
#    try:
#        return engine.startLoop() 
#    except Exception:
#        pass #handle nonsensical exception thrown ('nextfire'attribute error)
#
#def stopAndDeleteEngine(engine, thread):
#            engine.stop()
#            engine.endLoop()
#            thread.join()
#            del engine
#    
#def speaker(text):
#    engine = pyttsx3.init()
#    thread = threading.Thread(target=speak, args=(text,engine,)) # Always put a comma after the arguments. Even if you have only one arg.
#    thread.start() # Start the thread
#    return engine, thread
#    

