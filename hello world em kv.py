#encoding :utf-8
from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text ="Hello World")


hw=App()#diz que o nome da instancia é o hw

hw.build = build #associa o hw a função build mas sem executa-la para que ela só seja executada dentro do aplicativo quando o quesito for atendido com por exemplo chamar a tela

hw.run()#executa o codigo



#App().run()# faz a tela abrir e executa ela em geral abre apenas uma tela preta que contem as funções do sistema em execução
