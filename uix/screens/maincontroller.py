from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from uix.screens import welcomescreen, signinscreen, signupscreen, homescreen, resetpassword, guestscreen


class ScreenManage(ScreenManager):
    Builder.load_file('./uix/screens/themedwidgets.kv')

    def __init__(self, **kwargs):
        super(ScreenManage, self).__init__(**kwargs)
        self.transition = FadeTransition()
        self.pos_hint = {'top': 1, 'left': 1}

        sign_sc = signupscreen.SignupScreen(name="Signup")
        logi_sc = signinscreen.SigninScreen(name="Signin")
        welc_sc = welcomescreen.WelcomeScreen(name="Welcome")
        home_sc = homescreen.HomeScreen(name="Home")
        reset_sc = resetpassword.ResetScreen(name="Reset")
        guest_sc = guestscreen.GuestScreen(name="Guest")

        self.add_widget(welc_sc)
        self.add_widget(sign_sc)
        self.add_widget(reset_sc)
        self.add_widget(logi_sc)
        self.add_widget(home_sc)
        self.add_widget(guest_sc)


class NavigationBar(FloatLayout):

    def __init__(self, **kwargs):
        super(NavigationBar, self).__init__(**kwargs)
        # self.orientation = 'horizontal'


class MainControl(FloatLayout):

    def __init__(self, **kwargs):
        self.sm = ScreenManage()
        self.nav = NavigationBar()
        super(MainControl, self).__init__(**kwargs)
        self.pos = ('0dp', '0dp')
        self.size_hint = (None, None)
        self.width = '360dp'
        self.height = '640dp'

    Builder.load_string("""
<MainControl>:
    ScreenManage:
        id: screenmanage
        size_hint: None, None
        pos: '0dp', '584dp'
        width: '360dp'
        height: '584dp'
    
    NavigationBar:
        id: navbar
        size_hint: None, None
        pos: '0dp', '0dp'
        width: '360dp'
        height: '56dp'
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#ffffff")
            Rectangle:
                size: self.size
                pos: self.pos
        
        ThemedImageButton:
            source: "./data/menu1.png"
            pos: '24dp', '16dp'
        
        ThemedImageButton:
            source: "./data/user.png"
            pos: '96dp', '16dp'
        
        ThemedImageButton:
            source: "./data/chat.png"
            size_hint: None, None
            width: '28dp'
            height: '28dp'
            pos: '166dp', '14dp'
        
        ThemedImageButton:
            source: "./data/tips.png"
            pos: '240dp', '16dp'
        
        ThemedImageButton:
            source: "./data/location.png"
            pos: '312dp', '16dp'
    """)