# coding: utf-8

#GUI
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ListProperty

# Core
from .core import (speak, talk, recognise)
import random
from android.permissions import request_permissions, Permission

# Skills
from .skills import (time_date, exit, weather, music, screenshot, resay, wiki, location, weather_no_city,
                     translate, news, coin, brightness, battery, vibrate, search, open, ytvideo, poweroff, call,
                     todolist, shoplist, netconnection, guess_num, rulette, math, crystal_ball, random_num, timer,
                     old_skills, skill_loader)

# Ответы на неизвестную команду.
wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?",
         "Ты, наверное, ошибаешься. Я тебя не понимаю.",
         "Извини, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я тебя не понимаю.",
         "Пожалуйста, не говори слов, которых я незнаю.", "Ты пытаешься оскорбить меня этим?",
         "Не издевайся надо мной, я знаю не так много слов.", "Извини, я не могу тебя понять.", "А?",
         "Объясни попроще.",
         "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.",
         "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.",
         "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.")

randnum = -1
isGuessNum = False
isRuLette = False


class Message(MDLabel):
    background_color = ListProperty()

    def __init__(self, *args, **kwargs):
        MDLabel.__init__(self, *args, **kwargs)
        self.text_size = self.size
        self.size = self.texture_size


class VasisualyApp(MDApp):

    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.layoutscr = GridLayout(cols=1, spacing=45, size_hint_y=None)
        self.layoutscr.bind(minimum_height=self.layoutscr.setter('height'))
        
        scrv = ScrollView()
        scrv.add_widget(self.layoutscr)
        self.root.add_widget(scrv)
        
        gl = GridLayout(cols=3, size_hint=[1, 0.06], spacing=20)
        gl.add_widget(MDLabel(text='Вы:', size_hint_x=0.12))
        self.input = MDTextField(on_text_validate=self.vasmsg, text_validate_unfocus=False)
        gl.add_widget(self.input)
        send = MDRectangleFlatButton(size_hint_x=0.35, on_release=self.vasmsg)
        gl.add_widget(send)
        Window.softinput_mode = "pan"
        
        self.root.add_widget(gl)
        speak.speak('Привет, меня зовут Васисуалий. Чем могу быть полезен?', self.layoutscr)

        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_SETTINGS, Permission.CALL_PHONE,
                             Permission.READ_CONTACTS])

        return self.root

    def vasmsg(self, instance):
        self.say = self.input.text
        self.input.text = ''
        self.say = self.say.capitalize()
        usrMsg = Message(text=self.say, size_hint_y=None, halign="right")
        self.layoutscr.add_widget(usrMsg)
        self.program()
        
    def recogniser(self):
        self.say = recognise.recognise(self.layoutscr)
        self.program()

    def program(self):
        say = self.say
        skillUse = False
        
        if say == '' or say == ' ':
            pass
            
        elif guess_num.isTriggered(say):
            skillUse = True
            global isGuessNum, randnum
            randnum = guess_num.getRandomNum()
            isGuessNum = guess_num.startGame(self.layoutscr)
            
        elif rulette.isTriggered(say):
            skillUse = True
            global isRuLette
            isRuLette = rulette.startGame(self.layoutscr)
            
        elif old_skills.old_skills_activate(say, self.layoutscr):
            skillUse = True

        elif skill_loader.run_skills(say, self.layoutscr):
            skillUse = True
            
        elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
            pass
        
        elif isGuessNum:
            isGuessNum = guess_num.game(say, randnum, isGuessNum, self.layoutscr)
            
        elif isRuLette:
            isRuLette = rulette.game(say, self.layoutscr)
            
        else:
            if talk.talk(say) != "" and not skillUse:
                speak.speak(talk.talk(say), self.layoutscr)
            elif not skillUse:
                if say != "":
                    # Фразы для ответа на несуществующие команды
                    randwrong = random.choice(wrong)
                    speak.speak(randwrong, self.layoutscr)


def main():
    VasisualyApp().run()

if __name__ == '__main__':
    main()
