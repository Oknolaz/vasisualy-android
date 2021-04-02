# coding: utf-8

#GUI
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

# Core
from core import speak
from core import talk
from core import recognise
import plyer
import random

# Skills
from skills import time_date
from skills import exit
from skills import joke
from skills import weather
from skills import music
from skills import screenshot
from skills import resay
from skills import wiki
from skills import location
from skills import weather_no_city
from skills import translate
from skills import news
from skills import coin
from skills import brightness
from skills import battery
from skills import vibrate
from skills import search
from skills import open
from skills import ytvideo
from skills import poweroff
from skills import call
from skills import todolist
from skills import shoplist
from skills import netconnection
from skills import guess_num
from skills import rulette
from skills import math
from skills import crystal_ball

wrong = ("Прости, я тебя не понимаю.", "Мне кажется ты несёшь какой-то бред.", "Что?", "Ты, наверное, ошибаешься. Я тебя не понимаю.", "Извини, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я тебя не понимаю.", "Пожалуйста, не говори слов, которых я незнаю.", "Ты пытаешься оскорбить меня этим?", "Не издевайся надо мной, я знаю не так много слов.", "Извини, я не могу тебя понять.", "А?", "Объясни попроще.", "Пожалуйста, прочитай моё описание. Скорее всего я не умею делать то, что ты меня просишь или попробуй использовать синонимы.", "Ты ошибаешься.", "Я не понимаю твоего вопроса.", "Мне не понятен твой вопрос.", "Не могу понять о чём ты говоришь.", "Я не понимаю.", "О чём ты?", "Я не могу распознать вопрос.") # Ответы на неизвестную команду.

randnum = -1
isGuessNum = False
isRuLette = False


class VasisualyApp(MDApp):

    def build(self):
        self.root = BoxLayout(orientation = 'vertical')
        self.layoutscr = GridLayout(cols = 1, spacing = 3, size_hint_y = None)
        self.layoutscr.bind(minimum_height = self.layoutscr.setter('height'))
        
        scrv = ScrollView()
        scrv.add_widget(self.layoutscr)
        self.root.add_widget(scrv)
        
        gl = GridLayout(cols = 3, size_hint = [1, 0.06])
        gl.add_widget(MDLabel(text = 'Вы:', size_hint_x = 0.15))
        self.input = MDTextField(on_text_validate = self.vasmsg, text_validate_unfocus = False)
        gl.add_widget(self.input)
        send = MDRectangleFlatButton(size_hint_x = 0.2, on_release = self.vasmsg)
        gl.add_widget(send)
        
        self.root.add_widget(gl)
        speak.speak('Привет, меня зовут Васисуалий. Чем могу быть полезен?', self.layoutscr)
        
        return self.root


    def vasmsg(self, instance):
        self.say = self.input.text
        self.input.text = ''
        self.say = self.say.capitalize()
        usrMsg = MDLabel(text = self.say, size_hint_y = None, text_size = [self.layoutscr.width, None], halign = "right")
        self.layoutscr.add_widget(usrMsg)
        self.program()
        
    def recogniser(self):
        self.say = recognise.recognise(self.layoutscr)
        self.program()
        
    def keyboardVisible(self, instance, value):
        self.kbrd = MDLabel(text = "    ", size_hint = [1, 0.35])
        self.root.add_widget(self.kbrd)
        
    def hideKeyboard(self, instance, value):
        try:
            self.root.remove_widget(self.kbrd)
        except Exception:
            pass

    def program(self):
        say = self.say
        skillUse = False
        
        if say == '' or say == ' ':
            pass

        if time_date.main(say):
            speak.speak(time_date.main(say), self.layoutscr)
            skillUse = True
            
        elif exit.main(say):
            skillUse = True
            
        elif joke.main(say):
            speak.speak(joke.main(say), self.layoutscr)
            skillUse = True
            
        elif weather.main(say, self.layoutscr):
            skillUse = True
            
        elif weather_no_city.main(say, self.layoutscr):
            skillUse = True
            
        elif music.main(say, self.layoutscr):
            skillUse = True
            
        elif screenshot.main(say, self.layoutscr):
            skillUse = True
            
        elif resay.main(say, self.layoutscr):
            skillUse = True
            
        elif wiki.main(say, self.layoutscr):
            skillUse = True
            
        elif location.main(say, self.layoutscr):
            skillUse = True
            
        elif translate.main(say, self.layoutscr):
            skillUse = True
            
        elif news.main(say, self.layoutscr):
            skillUse = True
            
        elif coin.main(say, self.layoutscr):
            skillUse = True
            
        elif brightness.main(say, self.layoutscr):
            skillUse = True
            
        elif battery.main(say, self.layoutscr):
            skillUse = True
            
        elif vibrate.main(say, self.layoutscr):
            skillUse = True
            
        elif search.main(say, self.layoutscr):
            skillUse = True
            
        elif poweroff.main(say, self.layoutscr):
            skillUse = True
            
        elif ytvideo.main(say, self.layoutscr):
            skillUse = True
            
        elif open.main(say, self.layoutscr):
            skillUse = True
            
        elif call.main(say, self.layoutscr):
            skillUse = True
            
        elif todolist.main(say, self.layoutscr):
            skillUse = True
            
        elif shoplist.main(say, self.layoutscr):
            skillUse = True
            
        elif netconnection.main(say, self.layoutscr):
            skillUse = True
            
        elif guess_num.isTriggered(say):
            skillUse = True
            global isGuessNum, randnum
            randnum = guess_num.getRandomNum()
            isGuessNum = guess_num.startGame(self.layoutscr)
            
        elif rulette.isTriggered(say):
            skillUse = True
            global isRuLette
            isRuLette = rulette.startGame(self.listWidget)
            
        elif math.calculate(say, self.layoutscr):
            skillUse = True
            
        elif crystal_ball.main(say, self.layoutscr):
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
            
            
            
if __name__ == '__main__':
    VasisualyApp().run()
