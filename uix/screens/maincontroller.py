from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from uix.screens import welcomescreen, signinscreen, signupscreen, homescreen, resetpassword, guestscreen,\
    accountscreen, informationscreen, locatescreen


class ScreenManage(ScreenManager):
    Builder.load_file('./uix/screens/themedwidgets.kv')

    def __init__(self, **kwargs):
        super(ScreenManage, self).__init__(**kwargs)
        self.transition = FadeTransition()

        welc_sc = welcomescreen.WelcomeScreen(name="Welcome")
        logi_sc = signinscreen.SigninScreen(name="Signin")
        sign_sc = signupscreen.SignupScreen(name="Signup")
        home_sc = homescreen.HomeScreen(name="Home")
        reset_sc = resetpassword.ResetScreen(name="Reset")
        guest_sc = guestscreen.GuestScreen(name="Guest")
        account_sc = accountscreen.AccountScreen(name="User")
        info_sc = informationscreen.InformScreen(name="Tips")
        locate_sc = locatescreen.LocateScreen(name="Location")

        self.add_widget(welc_sc)
        self.add_widget(logi_sc)
        self.add_widget(sign_sc)
        self.add_widget(reset_sc)
        self.add_widget(guest_sc)
        self.add_widget(home_sc)
        self.add_widget(account_sc)
        self.add_widget(info_sc)
        self.add_widget(locate_sc)


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
    NavigationBar:
        id: navbar
        size_hint: None, None
        pos: ('0dp', '0dp' if screenmanage.current in ['Home', 'User', 'Tips', 'Location'] else  '-56dp')
        width: '360dp'
        height: '56dp' if screenmanage.current in ['Home', 'User', 'Tips', 'Location'] else '-56dp'
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#f5f5f5")
            Rectangle:
                size: self.size
                pos: self.pos
        
        ThemedImageButton:
            source: "./data/menu.png" if screenmanage.current != "Menu" else "./data/menub.png"
            pos: '24dp', '16dp'
            # on_release: screenmanage.current = "Menu"
        
        ThemedImageButton:
            source: "./data/user.png" if screenmanage.current != "User" else "./data/userb.png"
            pos: '96dp', '16dp'
            on_release: screenmanage.current = "User"
        
        ThemedImageButton:
            text: "chat"
            source: "./data/chat.png" if screenmanage.current != "Home" else "./data/chatb.png"
            pos: '168dp', '16dp'
            on_release: screenmanage.current = "Home"
        
        ThemedImageButton:
            source: "./data/tips.png" if screenmanage.current != "Tips" else "./data/tipsb.png"
            pos: '240dp', '16dp'
            on_release: screenmanage.current = "Tips"
        
        ThemedImageButton:
            source: "./data/location.png" if screenmanage.current != "Location" else "./data/locationb.png"
            pos: '312dp', '16dp'
            on_release: screenmanage.current = "Location"
    
    ScreenManage:
        id: screenmanage
        size_hint: None, None
        pos: ('0dp', '56dp') if self.current in ['Home', 'User', 'Tips', 'Location'] else ('0dp', '0dp')
        width: '360dp'
        height: '640dp'
    """)