#coding: utf-8

from kivy.app import App as app
from kivy.uix.floatlayout import FloatLayout as fl
from kivy.uix.button import Button as bt

class RootWidget(fl):
    pass


class MedApp(app):

    def build(self):
        return RootWidget()

MedApp().run()