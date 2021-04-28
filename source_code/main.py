#Using Kivy and KivyMD in this new App
#By KidGenius
import kivy
import kivymd
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.app import App
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.popup import Popup
from random import random
import webbrowser
import pickle
from re import *
import json
import sys

Window.size = (500, 600)

#Clock.max_iteration = 30

Alphabet_UP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
                ]
Alphabet_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

Special = ["!", "@", "#", "$", "%", "&", "?", "_", "{", "}"]

Pass_Dict = ["Pa$$w0rd321", "7632{b1@!", "$ecure p@ss246", "Be@rsbeets359", "p@sSwOrD#@", "3654@8!9#",
             "KiLLa_G@mer2341", "Re@L_G&gamer32", "$@FE_!P@$SWORD", "Chi{c}ken_$andw!ch", "N0n_Cr@c{kabl3",
             "uN(Rack@bl3", "Pr0t3ct@account456", "@ccouNt_$3cur{e}", "F@v0rit3s", "Ch1ck3n_Soup@#"
             ]

#Lists app will use to update the Dictionary
Gen_list = []
Val_list = []
Dict_list = []

#Generate screen place holder and variables
Gen_click_check = -1
Passwd = None
Clicked = 0

Password_file = open("Data/All_Passwords.txt", "a")
passwd_data = open("Data/passwds.json", "r")

Old_data = json.load(passwd_data)
update_data = Old_data.copy()


def update_dict(Dict, ID, passwd):
    if ID == "Val":
       Val_list.append(passwd)
       Dict["Val"] = Old_data["Val"] + Val_list
       file = open("Data/passwds.json", "w")
       json.dump(Dict, file)
       file.close()
    if ID == "Gen":
       Gen_list.append(passwd)
       Dict["Gen"] = Old_data["Gen"] + Gen_list
       file = open("Data/passwds.json", "w")
       json.dump(Dict, file)
       file.close()
    if ID == "Dict":
       Dict_list.append(passwd)
       Dict["Dict"] = Old_data["Dict"] + Dict_list
       file = open("Data/passwds.json", "w")
       json.dump(Dict, file)
       file.close()

       
       

     
class Val_help(GridLayout):
    cols = 1
    c = "Your password must have atleast:""\n""One uppercase letter""\n""Four lowercase letters""\n""Two numbers""\n""One special character(!@#)""\n""Example: Passwd12#"

class passwd_not_strong(GridLayout):
    cols = 1
    

class passwd_valid(GridLayout):
    cols = 1   


class Second_dict(GridLayout):
    cols = 1
    second = ObjectProperty(None)
    B = "* Your password has been saved"
    
class Dict_pop(GridLayout):
    import random
    cols = 1
    A = random.choice(Pass_Dict)
    b = "Please copy the password that has been provided for you.""\n""Press change to change your password.""\n""Press keep to save your password."
    
    dict_passwd1 = ObjectProperty(None)
    
    def pressed_change(self):
        import random
        A = random.choice(Pass_Dict)
        self.dict_passwd1.text = A

    def pressed_keep(self):
        Dictionary_Pop1()
        update_dict(update_data, "Dict", self.dict_passwd1.text)
        Password_file.write("Dictionary password: ""\n" + str(self.dict_passwd1.text) + "\n")

class MainScreen(Screen):
    pass

class Gen_passwd(GridLayout):
    #passwd1 = ObjectProperty(None)
    import random
    global Passwd
    store = None
    cols = 1
    
    def password(self):
        import random
        global Passwd
        print("yep")
        store = self.ids.passwd
        cols = 1  
        A = random.choices(Alphabet_UP, k = 4)
        B = random.choices(Alphabet_low, k = 4)
        C = random.choices(Numbers, k = 3)
        D = random.choices(Special, k = 2)
        a = A + B + C + D
        store.text = str(a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[6] + a[7] + a[8] + a[9] + a[10] + a[11] + a[12])
        Passwd = store.text
        Passwd2 = Passwd
        return store.text

    
class GenerateScreen(Screen):

    def gen_passwd(self):
        Password_file.write("Generate Password:""\n" + Passwd + "\n")


    def clicked_btn(self):
        generate_passwd()
        update_dict(update_data, "Gen", Passwd)     
    
class Dict_Screen(Screen):
    def btn(self):
        Dictionary_Pop()

class Validate(Screen):
    validate = ObjectProperty(None)
    Help = "To have a secure password:""\n""You must atleast have 1 uppercase letters.""\n""4 lowercase letters.""\n""2 numbers and""\n""and 1 special character""\n""Also it must be at least 8 chracaters long,but with these""\n""password rules.It is going to be 8 characters long."
    
   
    def pressed_validate(self):
        global Val_list, Passwds
        import re

        # Small method that validates the password
        a = self.validate.text
        # Remind = 0
        flag = 0
        if not re.search(str(Alphabet_UP), a):
            print("Up not there")
            flag = 1
        if not re.search(str(Alphabet_low)*4, a):
            print("low not there")
            flag = 1
        if not re.search(str(Numbers)*2, a):
            print("no. not there")
            flag = 1
        if not re.search(str(Special), a):
            print("special not there")
            flag = 1
            
            
        if flag == 1:
            Passwd_Not_Strong()
        if flag == 0:
            Passwd_Valid()
            self.validate.text = ""
            update_dict(update_data, "Val", a)
            Password_file.write("Validated password:""\n" + str(a) + "\n")


class About_Dev(Screen):
    pass

class About(Screen):
    pass

class Legal_Screen(Screen):
    a = "I wrote the code which makes my app work.But the code used to make the GUI and other functions were from the modules""\n""Kivy and Kivymd which use sdl2, glew, pygments, docutils which were not written by me. They are dependencies which are needed by kivy and kivymd to work.""\n""These dependecies may be copyrighted, so to confirm, I did not write the code to for those programs/dependencies""\n""If you are not satisfied with this license, please consult me before taking any legal action, I will gladly take down the app"
    b = "This is an open source program, so permission is hereby granted, free of charge , to copy, modify, and/or sell this program."

class Password_Screen(Screen):
    def Gen_list(self):
        passwd_data = open("Data/passwds.json", "r")
        gen_passwds = json.load(passwd_data)
        h = gen_passwds["Gen"]
        for i in range(len(h)):
            Items = TwoLineListItem(text="Generated Password:" ,secondary_text= str(i + 1) + ". " + str(h[i]))
            self.ids.Passwd_list.add_widget(Items)
        passwd_data.close()

            
    def Val_list(self):
        passwd_data = open("Data/passwds.json", "r")
        val_passwds = json.load(passwd_data)
        f = val_passwds["Val"]
        for i in range(len(f)):
            Items2 = TwoLineListItem(text="Validated Password:" ,secondary_text= str(i + 1) + ". " + str(f[i]))
            self.ids.Passwd_list.add_widget(Items2)
        passwd_data.close()

            
    def Dict_list(self):
        passwd_data = open("Data/passwds.json", "r")
        dict_passwds = json.load(passwd_data)
        a = dict_passwds["Dict"]
        for i in range(len(a)):
            Items3 = TwoLineListItem(text="Dictionary Password:" ,secondary_text= str(i + 1) + ". " + str(a[i]))
            self.ids.Passwd_list.add_widget(Items3) 
        passwd_data.close()


    

    

# where all popup windows are
def Dictionary_Pop():
    # Dictionary popup window
    pop = Dict_pop()
    popupWindow = Popup(title="Get password", content=pop, size_hint=(None, None), size=(350,400))
    popupWindow.open()

def Dictionary_Pop1():
    # Dictionary popup window
    pop1 = Second_dict()
    popupWindow1 = Popup(title="Password", content=pop1, size_hint=(None, None), size=(400,150))
    popupWindow1.open()

def validate_help():
    show5 = Val_help()
    showWin = Popup(title="Password help", content=show5, size_hint=(None,None), size=(500, 380))
    showWin.open()

def Passwd_Not_Strong():
    # Validate popup window
    show = passwd_not_strong()
    popupWin = Popup(title="Password not strong enough", content=show, size_hint=(None,None), size=(400,200))
    popupWin.open()

def Passwd_Valid():
    show2 = passwd_valid()
    popupWin2 = Popup(title="Password is valid", content=show2, size_hint=(None,None), size=(400, 150))
    popupWin2.open()

def generate_passwd():
    show6 = Gen_passwd()
    PopScreen = Popup(title ="Password Generated:" ,content=show6,size_hint=(None,None), size=(350, 200))
    PopScreen.open()

SM = ScreenManager()
SM.add_widget(MainScreen(name="main"))


class PasswordApp(MDApp):
        
    def build(self):
        self.icon = "Data/Password_icon.png"
        self.title = "Password Generator and Validator"
        return
    
    def Main_screen(self):
        self.root.current = "main"

    def Gen_screen(self):
        self.root.current = "Gen"

    def open(self, ID):
        if ID == "Youtube":
            webbrowser.open("https://www.youtube.com/channel/UC5lglvyKbrD0mYE2pcw8gsQ")
        if ID == "Instagram":
            webbrowser.open("https://www.instagram.com/kid_genius3214/")
        if ID == "Paypal":
            webbrowser.open("https://paypal.me/TshifhiwaMadula?locale.x=en_US")

if __name__ == "__main__":
    PasswordApp().run()


Password_file.close()
