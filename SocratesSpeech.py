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
from difflib import SequenceMatcher

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
    for (dirpath, dirnames, filenames) in walk('./protocols'):
        folder.extend(filenames)
        break
    result = [SequenceMatcher(a=triggerWord,b=files.lower()).quick_ratio()for files in folder] #s.set_seq2(files.lower())
    bestMatch = result.index(max(result))
    return folder[bestMatch]

def openFile(triggerWord):
    path = findFile(triggerWord)
    with open('./protocols/'+ path, 'r') as file:
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


