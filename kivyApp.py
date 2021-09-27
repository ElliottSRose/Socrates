#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:01:49 2020

@author: elliott
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from SocratesSkills import *
#
#
#from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.scrollview import ScrollView
#from kivy.properties import StringProperty
#from kivy.lang import Builder
#
#long_text = wikiAnswer('Socrates')
#
#Builder.load_string('''
#<ScrollableLabel>:
#    Label:
#        size_hint_y: None
#        height: self.texture_size[1]
#        text_size: self.width -10, None
#        text: root.text
#''')
#
#class ScrollableLabel(ScrollView):
#    text = StringProperty('')
#    
class MyGrid(Widget):
    query = ObjectProperty(None)
    
    def btn(self):
        print(wikiAnswer(self.query.text))
        print("Query: ", self.query.text)
        self.query.text = ""
        self.textLabel.text=str(wikiAnswer(self.query.text))

class MyApp(App):
    def build(self):
        return MyGrid()
#
def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
#    
if __name__ =="__main__":
    reset()   
    MyApp().run()


#<ScrollView>:
#    do_scroll_x: False
#    do_scroll_y: True
#
#    Label:
#        size_hint_y: None
#        height: self.texture_size[1]
#        text_size: self.width
#        padding: 20, 20
#

##class ScrollApp(App):
#    def build(self):
#        return ScrollableLabel(text=long_text)
#
#if __name__ == "__main__":
#    reset()
#    ScrollApp().run()
    
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.button import Button
#from kivy.uix.scrollview import ScrollView
#from kivy.core.window import Window
#from kivy.app import runTouchApp
#
#
#layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
## Make sure the height is such that there is something to scroll.
#layout.bind(minimum_height=layout.setter('height'))
#btn = Button(text='Start Socrates', size_hint_y=None, height=40)
#layout.add_widget(Label(text='What can I do for you?'))
#layout.add_widget(btn)
#
#root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
#root.add_widget(layout)
#
#runTouchApp(root)