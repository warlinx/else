import re

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

from store import ip

print(re.search(b'\d+\.\d+\.\d+\.\d+', ip).group())
