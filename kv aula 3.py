#coding: utf-8

#aprendendo sobre outros widgets

from kivy.app import App
from kivy.uix.button import Button
def prin():
    print ("deu certo")


def build():
    bt = Button(text="Comprar")
    bt.on_press = prin
    return bt


# o evento on press tem a mesma função que i comando self.btn.clicke.connet no pyqt ele amarra o click a um evento

app = App()
app.build = build
app.run()