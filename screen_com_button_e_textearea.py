#coding: utf-8
#author:nox

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def click():
    print(ed.text)


def build():
    layout = RelativeLayout()

    ed = TextInput(text="teste")
    ed =ed.global
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.y = 250
    ed.x = 90


    btn = Button(text="Clique aqui")
    btn.size_hint = None, None
    btn.width = 200
    btn.height = 50
    btn.y = 150
    btn.x = 200
    btn.on_press= click()
    layout.add_widget(ed)
    layout.add_widget(btn)

    return layout
#antes de posicionar um componente deve se dizer as dimensões dele

wind = App()
from kivy.core.window import Window
wind.title="Testes"
Window.size = 600, 600
wind.build = build
wind.run()

