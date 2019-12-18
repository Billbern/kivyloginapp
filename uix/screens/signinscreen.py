from kivy.lang import Builder
from db import MainDataB, verify_password
from kivy.uix.screenmanager import Screen


class SigninScreen(Screen):
    def __init__(self, name, **kwargs):
        super(SigninScreen, self).__init__(**kwargs)
        self.name = name

    def login(self):
        self.ids.id_label.text = " "
        if len(self.ids.id_email.text) < 1 or len(self.ids.id_pass.text) < 1:
            self.ids.id_label.text = "Please fill email and password field"
        else:
            usermail = MainDataB.database.users.find_one({'email': self.ids.id_email.text})
            username = MainDataB.database.users.find_one({'fname': self.ids.id_email.text})
            if usermail or username:
                if verify_password(username["password"], self.ids.id_pass.text) or \
                        verify_password(usermail["password"], self.ids.id_pass.text):
                    self.parent.current = "Home"
                else:
                    self.ids.id_label.text = "Wrong email or password"
            else:
                self.ids.id_label.text = "Wrong email or password"
    Builder.load_string("""
    
<SigninScreen>:
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
            
        Label:
            text: '[color=34ace0][b]Signin[/b][/color]'
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
            id: id_email
            hint_text: "Email or Username"
            pos: "50.5dp", "395dp"
            
        ThemedInput:
            id: id_pass
            password: True
            hint_text: "Password"
            pos: "50.5dp", "309dp"
        
        ThemedLabelButton:
            text: "[color=3e3e3e]Forget Password ?[/color]"
            pos: "210dp", "266dp"
            width: "100dp"
            height: "22dp"
            on_release: root.parent.current= 'Reset'
        
        ThemedButton:
            text: '[b]Signin[/b]'
            pos: "50.5dp","202dp"
            on_press: root.login()
        
        ThemedButton:
            text: '[b]Signup[/b]'
            pos: "50.5dp","96dp"
            on_release: root.parent.current= 'Signup'
            
        ThemedLabelButton:
            text: "[color=3e3e3e] or continue as a[/color]  [color=34ace0][size=15][b]Guest[/b][/size][/color]"
            pos: "50.5dp", "32dp"
            width: "259dp"
            height: "46dp"
            on_release: root.parent.current= 'Guest'

        
    """)
