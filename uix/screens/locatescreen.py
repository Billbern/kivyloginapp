from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class LocateScreen(Screen):
    isShownMenu = BooleanProperty(False)

    def __init__(self, name, **kwargs):
        super(LocateScreen, self).__init__(**kwargs)
        self.name = name

    Builder.load_string("""
#:import utils kivy.utils
#:import Mapview kivy.garden.mapview

<LocateScreen>:
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
        
        MapView:
            pos: '0dp', '56dp'
            zoom: 11
            lat: 50.6394
            lon: 3.057
    """)