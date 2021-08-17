# coding: utf-8

# GUI
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList
from kivymd.uix.dialog import MDDialog
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior

# Core
from .core import (speak, talk, recognise)
import random
from jnius import autoclass, cast
from android.permissions import request_permissions, Permission
import os

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

skill_loader.load()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Вызывается, когда происходит нажатие на элемент меню.'''

        # Задаёт цвет иконки и текста для каждого элемента меню.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class AboutScreen(Screen):
    def source_code_open(self):
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        Intent = autoclass("android.content.Intent")
        Uri = autoclass("android.net.Uri")
        # Создание Intent'а.
        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)

        intent.setData(Uri.parse("https://github.com/Oknolaz/vasisualy"))

        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(intent)  # Запуск Intent'а (открытие ссылки).

    def issues_open(self):
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        Intent = autoclass("android.content.Intent")
        Uri = autoclass("android.net.Uri")
        # Создание Intent'а.
        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)

        intent.setData(Uri.parse("https://github.com/Oknolaz/vasisualy/issues/"))

        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(intent)  # Запуск Intent'а (открытие ссылки).

    def license_open(self):
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        Intent = autoclass("android.content.Intent")
        Uri = autoclass("android.net.Uri")
        # Создание Intent'а.
        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)

        intent.setData(Uri.parse("https://www.gnu.org/licenses/gpl-3.0.html"))

        currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
        currentActivity.startActivity(intent)  # Запуск Intent'а (открытие ссылки).


class MainScreen(Screen):
    def __init__(self, *args, **kwargs):
        Screen.__init__(self, *args, **kwargs)
        speak.speak('Привет, меня зовут Васисуалий. Чем могу быть полезен?', self.ids.layoutscr)

    def no_settings(self):
        # Вызывается при нажатии на иконку настроек.
        # Показывает диалог с сообщением о временном отсутствии настроек приложения.
        dialog = MDDialog(
            text="Извините, на данный момент настройки приложения недоступны.",
            buttons=[
                MDFlatButton(
                    text="OK"
                ),
            ],
        )
        dialog.open()

    def vasmsg(self):
        self.say = self.ids.input.text
        self.ids.input.text = ''
        self.say = self.say.capitalize()
        # Создание виджета с сообщением пользователя
        usrMsg = MDLabel(
            text=self.say,
            halign="right",
            size_hint_x=1
        )
        self.ids.layoutscr.add_widget(usrMsg) if self.say else None
        self.program()

    def recogniser(self):
        self.say = recognise.recognise(self.ids.layoutscr)
        self.program()

    def program(self):
        say = self.say
        skillUse = False

        if say == '' or say == ' ':
            pass

        elif os.path.exists(".skill_lock"):
            # Если файл блокировки существует - сообщение пользователя
            # передаётся запущенному циклу навыка.
            skill_loader.run_looped(say, self.listWidget)
            skillUse = True

        elif skill_loader.run_skills(say, self.ids.layoutscr):
            skillUse = True

        elif guess_num.isTriggered(say):
            # Игра в "Угадай число".
            skillUse = True
            global isGuessNum, randnum
            randnum = guess_num.getRandomNum()
            isGuessNum = guess_num.startGame(self.ids.layoutscr)

        elif rulette.isTriggered(say):
            # Игра в Русскую рулетку.
            skillUse = True
            global isRuLette
            isRuLette = rulette.startGame(self.ids.layoutscr)

        elif old_skills.old_skills_activate(say, self.ids.layoutscr):
            skillUse = True

        elif say == 'stop' or say == 'Stop' or say == 'Стоп' or say == 'стоп':
            pass

        elif isGuessNum:
            isGuessNum = guess_num.game(say, randnum, isGuessNum, self.ids.layoutscr)

        elif isRuLette:
            isRuLette = rulette.game(say, self.ids.layoutscr)

        else:
            if talk.talk(say) != "" and not skillUse:
                speak.speak(talk.talk(say), self.ids.layoutscr)
            elif not skillUse:
                if say != "":
                    # Фразы для ответа на несуществующие команды
                    randwrong = random.choice(wrong)
                    speak.speak(randwrong, self.ids.layoutscr)


class VasisualyApp(MDApp):

    def build(self):
        Window.softinput_mode = "pan"

        # Загрузка "экранов" GUI
        self.load_kv("vasisualy/ui/MainScreen.kv")
        self.load_kv("vasisualy/ui/AboutScreen.kv")
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(MainScreen(name="main"))
        self.screen_manager.add_widget(AboutScreen(name="about"))

        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_SETTINGS, Permission.CALL_PHONE,
                             Permission.READ_CONTACTS])  # Запрос необходимых разрешений у системы Android.

        return self.screen_manager

    def back_to_main(self):
        self.screen_manager.current = "main"


def main():
    VasisualyApp().run()


if __name__ == '__main__':
    main()
