import os
import hashlib
import binascii
from kivy.lang import Builder
from pymongo import MongoClient
from bson.objectid import ObjectId
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
        # survey_sc = surveyscreen.SurveyScreen(name="Survey")

        self.add_widget(welc_sc)
        self.add_widget(sign_sc)
        self.add_widget(reset_sc)
        self.add_widget(logi_sc)
        self.add_widget(home_sc)
        self.add_widget(guest_sc)
        # self.add_widget(account_sc)
        # self.add_widget(survey_sc)


class MainControl(FloatLayout):

    def __init__(self, **kwargs):
        self.sm = ScreenManage()
        super(MainControl, self).__init__(**kwargs)
        self.pos_hint = {'top': 1, 'left': 1}
        self.size_hint = (1, 1)

    Builder.load_string("""
<MainControl>:
    ScreenManage:
        id: screenmanage
    """)