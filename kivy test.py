__author__ = 'Jarrod'

import kivy
kivy.require('1.8.0') # replace with your current kivy version !


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class FormInput(GridLayout):

    def __init__(self, **kwargs):
        super(FormInput, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Song Title'))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)
        self.add_widget(Label(text='Artist'))
        self.artist = TextInput(multiline=False)
        self.add_widget(self.artist)


class MyFormApp(App):

    def build(self):
        return FormInput()


if __name__ == '__main__':
    MyFormApp().run()