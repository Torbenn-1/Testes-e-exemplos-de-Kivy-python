#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text="test de var com label"
    lb.italic = True
    lb.font_size = 50
    return lb


app = App()
app.build = build
app.run()

#as propriedade de um widget podem ser alteradas durante o tempo de execução e também pode ser enviadas como argumentos
#pode haver de termos que definir a propriedade antes da instancia ser criada
