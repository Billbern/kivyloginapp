from db import MainDataB
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class ResetScreen(Screen):
    def __init__(self, name, **kwargs):
        super(ResetScreen, self).__init__(**kwargs)
        self.name = name

    def reset(self):
        self.ids.id_label.text = " "
        if len(self.ids.id_email.text) < 1:
            self.ids.id_label.text = "Please fill in your email"
        else:
            if not MainDataB.database.users.find_one({'email': self.ids.id_email.text}):
                self.ids.id_label.text = "Email is not registered"
            else:
                self.parent.current = "Signin"

    Builder.load_string("""
    

<ResetScreen>:
    FloatLayout:
        pos_hint: {"top": 1, 'left': 1}
        size_hint: None, None
        width: self.parent.width
        height: self.parent.height
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#FFFFFF")
            Rectangle:
                size: self.size
                pos: self.pos
                
        ThemedImageButton:
            source: "./data/arrow.png"
            pos: "11dp", "605dp"
            on_release: root.parent.current= 'Signin'
        
        Label:
            text: '[color=34ace0][b]Reset Password[/b][/color]'
            markup: True
            pos: "105dp", "524dp"
            font_size: '24sp'
            size_hint: None, None
            width: '76dp'
            height: '32dp'
        
        Label:
            id: id_label
            color: utils.get_color_from_hex("#b33939")
            pos: "53dp", "443dp"
            font_size: '12sp'
            size_hint: None, None
            width: '259dp'
            height: '48dp'

        ThemedInput:
            id: id_email
            hint_text: "Email"
            pos: "50.5dp", "395dp"

        ThemedButton:
            text: '[b]Reset Password[/b]'
            pos: "50.5dp","202dp"
            on_release: root.reset()

    """)
