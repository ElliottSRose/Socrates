#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:56:39 2020

@author: elliott
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
# from kivy.clock import mainthread
from Socrates import *
from queue import Queue
import threading      

def testFunc():
    return 5

class MyGrid(GridLayout):
    def __init__(self, **kwargs):        
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.q = Queue()
        
        self.submit = Button(text="Press anywhere for Socrates", font_size = 40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    # @mainthread  
    def pressed(self,instance):
        if self.submit.text != "Stop":
            self.submit.text = "Stop"
            thread = threading.Thread(target=startSocrates,args=(self.q,))
            thread.start() 
            #maybe i should try tracking the thread ID
        elif self.submit.text == "Stop":
            self.submit.text = "Stopping..."
            try:
                print('Putting stopper')
                self.q.put_nowait('stop')
                print('Stopper placed')
            except: 
                pass
        else:
            print(thread)
            print('thread information should be printing')
            print(thread.is_alive)
            while True:
                if thread.is_alive()==False:
                    print('thread isn''t alive, attempting to join')
                    thread.join()
                    print('thread stopped')
                    self.submit.text = "Press anywhere for Socrates" 
                else:
                    print('Thread is still alive')      
                
class MyApp(App):
    def build(self):
        return MyGrid()
    
def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
        
if __name__=="__main__":
    reset()
    MyApp().run()
    