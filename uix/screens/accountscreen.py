from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class AccountScreen(Screen):
    isShownMenu = BooleanProperty(False)

    def __init__(self, name, **kwargs):
        super(AccountScreen, self).__init__(**kwargs)
        self.name = name

    Builder.load_string("""
#:import utils kivy.utils

<AccountScreen>:
    FloatLayout:
        pos: ("-178dp" if root.isShownMenu else "0dp", "0dp") 
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