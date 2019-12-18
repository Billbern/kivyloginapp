from kivy.properties import BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class HomeScreen(Screen):
    isShownMenu = BooleanProperty(False)

    def __init__(self, name, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.name = name

    Builder.load_string("""
#:import utils kivy.utils

<HomeScreen>:
    # kree: btn
                
    FloatLayout:
        pos: ("182.5dp" if root.isShownMenu else "360dp", "0dp" )
        size_hint: None, None
        width: self.parent.width
        height: self.parent.height
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#89d4fb")
            Rectangle:
                size: self.size
                pos: self.pos
        
        ThemedImageButton:
            source: "./data/profile.png"
            pos: "188dp", "246dp"
        
        Label:
            text: "Profile"
            pos: "229dp", "246dp"
            size_hint: None, None
            width: "137dp"
            height: "35dp"
            font_size: "15sp"
            color: utils.get_color_from_hex("#3e3e3e")
        
        ThemedImageButton:
            source: "./data/tips.png"
            pos: "188dp", "171dp"
        
        Label:
            text: "Health Tips"
            pos: "228dp", "163dp"
            size_hint: None, None
            width: "119dp"
            height: "39dp"
            font_size: "15sp"
            color: utils.get_color_from_hex("#3e3e3e")
        
            
        ThemedImageButton:
            source: "./data/hospital.png"
            pos: "188dp", "20dp"
        
        Label:
            text: "Health Facilities"
            pos: "228dp", "20dp"
            size_hint: None, None
            width: "119dp"
            height: "39dp"
            font_size: "15sp"
            color: utils.get_color_from_hex("#3e3e3e")
        
    
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

        ThemedImageButton:
            source: "./data/close.png" if root.isShownMenu else "./data/menu.png"
            pos: ("322dp" if not root.isShownMenu else "144dp", "20dp")
            on_release: root.isShownMenu = not root.isShownMenu
    """)



