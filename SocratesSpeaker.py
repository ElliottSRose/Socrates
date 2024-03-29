#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:39:05 2020

@author: elliott
"""
import pyttsx3
import threading

class Speaker():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.thread = None

    def speak(self,text):
        self.engine.setProperty('voice','com.apple.speech.synthesis.voice.daniel')
        self.engine.say(text, 'Answer')
        try:
            self.engine.startLoop()
        except Exception:
            pass #handle exception thrown ('nextfire'attribute error)

    def stop(self):
        self.engine.stop()
        self.engine.endLoop()# causing kivy to crash
        self.thread.join()

    def speaker(self,text):
        self.thread = threading.Thread(target=self.speak, args=(text, ), daemon=True) # Always put a comma after the arguments. Even if you have only one arg.
        self.thread.start() # Start the thread
        return

s = Speaker()
# try without threading
s.speak("hello")

# s.speaker('hello')
# s.speaker("hello my friends in the south,Many of us take our computers for granted these days. Computers have become ubiquitous in society and its functions. Because of this, we have come to view computers as a certain thing that we are used to, and for most that is the desktop, laptop, and the cellphone. These devices have operating systems that guide us in our interactions with the computer, and thus influence those interactions. The study of Human Computer Interaction revolves around those relationships,")
