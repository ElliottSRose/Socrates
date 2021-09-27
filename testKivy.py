#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 08:56:51 2020

@author: elliott
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from random import choice
from time import sleep

xWords = ["hello1", "hello2", "hello3", "hello4", "hello5"]

class Test(GridLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.cols = 1
        for x in range(2):
            # I want it to show frist word then sleep 2 sec then clear first word from screen then print second word
            self.add_widget(Label(text = "[b]"+choice(xWords)+"[/b]", markup = True, font_size = "40sp"))
            sleep(2)
        # then clear all words in screen
        for x in range(5):
            # then show the new 4 words
            self.add_widget(Label(text = "[b]"+choice(xWords)+"[/b]", markup = True, font_size = "40sp"))

class TestApp(App):
    def build(self):
        return Test()

if __name__ == "__main__":
    TestApp().run()