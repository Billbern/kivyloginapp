import os
from kivy.app import App
os.environ['KIVY_METRICS_DENSITY'] = '1'
from kivy.core.window import Window
from uix.screens.maincontroller import MainControl


class MainApp(App):
    def build(self):
        return MainControl()


if __name__ == "__main__":
    Window.size = (360, 640)
    MainApp().run()
