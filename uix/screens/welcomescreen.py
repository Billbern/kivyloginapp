from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock


# class LogoAnime(Image):
#     def __init__(self, **kwargs):
#         super(LogoAnime, self).__init__(**kwargs)
#         self.source = "./data/Mbot.png"
#         self.pos = ("106.5dp", "225dp")
#         self.size = ("147dp", "59dp")
#
#         self.animation = Animation(pos=(106.5, None), d=0.7, t='out_cubic')
#         self.animation += Animation(pos=(217, None), d=.7)
#         self.animation += Animation(pos=(106.5, None), d=1, t='linear')
#         self.animation.repeat = True
#         self.animation.start(self)


class WelcomeScreen(Screen):
    def __init__(self, name, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.switch, 2)
        self.name = name

    def switch(self, *args):
        self.manager.current = "Signin"

    Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
    
<WelcomeScreen>:
    FloatLayout:
        pos_hint: {"top": 1, 'left': 1}
        size_hint: None, None
        width: self.parent.width
        height: self.parent.height
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#ffffff")
            Rectangle:
                size: self.size
                pos: self.pos
        

    """)