#coding: utf-8
from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="textinput test")


window = App()
window.build = build
window.run()