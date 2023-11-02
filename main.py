# https://yandex.ru/video/preview/13198009012106879976

import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return  Button(text="Hi")

# Press the green button in the gutter to run the script/z
if __name__ == '__main__':
    MyApp().run()

