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
from skills import flash

is_paused = False
isGuessNum = False
guesstry = 0
isRoulette = False
bullet = random.choice([0, 0, 0, 0, 0, 1])

wrong = ("Простите, я вас не понимаю.", "Мне кажется вы несёте какой-то бред.", "Что?", "Вы, наверное, ошиблись. Я вас не понимаю.", "Извините, я появился совсем недавно, я пока понимаю очень мало слов.", "Чего?", "А? Что? Я Вас не понимаю.", "Пожалуйста, не говорите слов, которых я незнаю.", "Вы пытаетесь оскорбить меня этим?", "Не издевайтесь надо мной, я знаю не так много слов.", "Извините, я не могу Вас понять.", "А?", "Объясните попроще.", "Пожалуйста, прочитайте моё описание. Скорее всего я не умею делать то, что вы меня просите или попробуйте использовать синонимы.", "Вы ошиблись.") # Ответы на неизвестную команду.
guessnum = ("Угадай число", "угадай число", "Поиграем в число", "поиграем в число", "Играть в угадай число", "играть в угадай число", "Играть в число", "играть в число", "Угадать число", "угадать число", "Угадывать число", "угадывать число")
russian_roulette = ("Русская рулетка", "русская рулетка", "В русскую рулетку", "в русскую рулетку")



class VasisualyApp(MDApp):

    def build(self):
        self.guessTry = 0
        self.isGuessNum = False
        randnum = 0
        self.isRoulette = False
        
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
        self.say.capitalize()
        usrMsg = MDLabel(text = self.say, size_hint_y = None, text_size = [self.layoutscr.width, None], halign = "right")
        self.layoutscr.add_widget(usrMsg)
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
        say = self.say.capitalize()
        skillUse = False
        if say == '' or say == ' ':
            pass
        
        for i in guessnum:
            if i in say:
                global randnum
                randnum = random.randint(0, 100)
                speak.speak("Я загадал число от 0 до 100. Угадай его.", self.layoutscr)
                self.isGuessNum = True
                skillUse = True
                guessTry = 0
                break
            
        for i in russian_roulette:
            if i in say:
                global isRoulette
                skillUse = True
                bullet = random.choice([0, 0, 0, 0, 0, 1])
                speak.speak("Я первый стреляю, если хочешь выстрелить - скажи \"выстрел\".", self.layoutscr)
                self.isRoulette = True
                if bullet == 1:
                    #media=music.inst.media_new("assets/shot.wav")
                    #music.player.set_media(media)
                    #music.player.play()
                    speak.speak("Ты выиграл.", self.layoutscr)
                    isRoulette = False
                else:
                    #media=music.inst.media_new("assets/misfire.wav")
                    #music.player.set_media(media)
                    #music.player.play()
                    speak.speak("Выстрела нет. Твоя очередь.", self.layoutscr)

        if time_date.main(say) != "":
            speak.speak(time_date.main(say), self.layoutscr)
            skillUse = True
            
        elif exit.main(say) != "":
            skillUse = True
            
        elif joke.main(say) != "":
            speak.speak(joke.main(say), self.layoutscr)
            skillUse = True
            
        elif weather.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif weather_no_city.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif music.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif screenshot.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif resay.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif wiki.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif location.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif translate.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif news.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif coin.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif brightness.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif battery.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif vibrate.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif search.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif poweroff.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif ytvideo.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif open.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif call.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif todolist.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif shoplist.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif flash.main(say, self.layoutscr) != "":
            skillUse = True
            
        elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
            pass
        
        elif self.isGuessNum:
            usrnum = -1
            try:
                usrnum = int(say)
            except Exception:
                pass
            if usrnum == -1:
                pass
            elif usrnum < randnum:
                speak.speak("Моё число больше.", self.layoutscr)
                self.guessTry += 1
            elif usrnum > randnum:
                speak.speak("Моё число меньше.", self.layoutscr)
                self.guessTry += 1
            elif usrnum == randnum:
                speak.speak(f"Поздравляю, ты выиграл затратив на это {str(self.guessTry+1)} попытки.", self.layoutscr)
                isGuessNum = False
                self.guessTry = 0
                
        elif self.isRoulette:
            if say == "Выстрел":
                bullet = random.choice([0, 0, 0, 0, 0, 1])
                if bullet == 1:
                    speak.speak("Ты проиграл.", self.layoutscr)
                    #media = music.inst.media_new("assets/shot.wav")
                    #music.player.set_media(media)
                    #music.player.play()
                    self.isRoulette = False
                else:
                    #media = music.inst.media_new("assets/misfire.wav")
                    #music.player.set_media(media)
                    #music.player.play()
                    speak.speak("Кручу барабан...", self.layoutscr)
                    bullet = random.choice([0, 0, 0, 0, 0, 1])
                    if bullet == 1:
                        speak.speak("Ты выиграл.", self.layoutscr)
                        #media = music.inst.media_new("assets/shot.wav")
                        #music.player.set_media(media)
                        #music.player.play()
                        self.isRoulette = False
                    else:
                        #media = music.inst.media_new("assets/misfire.wav")
                        #music.player.set_media(media)
                        #music.player.play()
                        speak.speak("Теперь ты.", self.layoutscr)
            
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
