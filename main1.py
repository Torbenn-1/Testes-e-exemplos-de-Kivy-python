#coding: utf-8

from kivy.app import App as app

class HelloApp(app):
    pass


HelloApp().run()
#o kv funciona da seguinte forma sempre que uma classe é criada ele verifica se tem algum arquivo com o mesmo nome e importa ele  (porém o nome tem que ser igual sem o sulfixo "APP" e deve estar em minusculo)
