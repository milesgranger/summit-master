# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button

from mobile.screens import LoginScreen

class SummitMaster(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    app = SummitMaster()
    app.run()
