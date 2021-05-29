#coding: utf-8

from kivy.app import App as app
from kivy.uix.label import Label as lb

class MyProg(app):
    def build(self):
       return lb()


MyProg().run()
#nesse caso a aplicação só começa apos instanciar a classe e executar a mesma