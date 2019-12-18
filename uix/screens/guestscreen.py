from kivy.lang import Builder
from db import MainDataB, Users
from kivy.uix.screenmanager import Screen


class GuestScreen(Screen):
    def __init__(self, name, **kwargs):
        super(GuestScreen, self).__init__(**kwargs)
        self.name = name

    def guestup(self):
        self.ids.id_label.text = " "
        account = Users(user_id=None, fname=self.ids.id_name.text, email="guest@healthalgo.com",
                        password=self.ids.id_pass.text)
        if len(self.ids.id_name.text) < 1 or len(self.ids.id_pass.text) < 1 or len(self.ids.id_conf.text) < 1:
            self.ids.id_label.text = "Please fill all Spaces"
        else:
            if self.ids.id_pass.text != self.ids.id_conf.text:
                self.ids.id_label.text = "Passwords don't match"
            else:
                if MainDataB.database.users.find_one({'fname': self.ids.id_name.text}):
                    self.ids.id_label.text = "Username is already in use"
                else:
                    MainDataB.database.users.insert(account.get_as_json())
                    self.ids.id_label.text = "Account Created"
                    self.parent.current = "Signin"

    Builder.load_string("""

<GuestScreen>:
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
            text: '[color=34ace0][b]Guest[/b][/color]'
            markup: True
            pos: "142dp", "524dp"
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
            id: id_name
            hint_text: "Username"
            pos: "50.5dp", "396dp"
        
        ThemedInput:
            id: id_pass
            password: True
            hint_text: "Password"
            pos: "50.5dp", "313dp"
            
        ThemedInput:
            id: id_conf
            password: True
            hint_text: "Confirm Password"
            pos: "50.5dp", "230dp"

        ThemedButton:
            text: '[b]Create[/b]'
            pos: "50.5dp","123dp"
            on_release: root.guestup()

    """)
