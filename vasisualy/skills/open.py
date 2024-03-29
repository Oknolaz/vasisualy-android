from ..core import speak
import plyer
from jnius import autoclass, cast

launch = ("Интернет", "интернет", "Браузер", "браузер", "Сеть", "сеть", "Включи интернет", "включи интернет",
          "Открой браузер", "открой браузер", "Включи браузер", "включи браузер", "Открой интернет", "открой интернет",
          "Включи сеть", "включи сеть", "Включи интернет сеть", "включи интернет сеть", "Всемирная паутина",
          "всемирная паутина", "Открой сеть", "открой сеть", "Подключись", "подключись", "Подключи", "подключи",
          "Подключи меня к сети", "подключи меня к сети", "Подключи сеть", "подключи сеть", "Подключи интернет",
          "подключи интернет", "Открой", "открой", "Запусти", "запусти", "Запуск", "запуск", "Программа", "программа",
          "Приложение", "приложение", "Включи", "включи")  # Команды открытия чего-либо

excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися",
               "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий",
               "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in launch:
        if i in say:

            for net in ("Браузер", "браузер", "Интернет", "интернет", "Сеть", "сеть", "Паутина", "паутина"):
                if net in say:
                    try:
                        # Открытие браузера
                        toSpeak = "Я открыл браузер."

                        open_url("https://github.com/Oknolaz/vasisualy")
                    except Exception:
                        toSpeak = "Не удалось открыть веб-браузер"
                            
            for yt in ("Youtube", "youtube", "Ютуб", "ютуб", "Ютьюб", "ютьюб", "Ютюб", "ютюб", "Утуб", "утуб"):
                if yt in say:
                    try:
                        open_url("https://youtube.com/")

                        toSpeak = "Открываю YouTube."
                    except Exception:
                        toSpeak = "Не удалось открыть YouTube."
                            
            for win in ("Окно", "окно", "Окошко", "окошко", "Дверь", "дверь", "Замок", "замок"):
                if win in say:
                    toSpeak = "Очень смешно..."
                    
            for fm in ("Файловый менеджер", "файловый менеджер", "Файлы", "файлы"):
                if fm in say:
                    toSpeak = "Открываю файловый менеджер."
                    try:
                        subprocess.run(["xdg-open", "/"])
                    except Exception:
                        toSpeak = "Не удалось открыть файловый менеджер."
                            
            for game in ("Игру", "игру", "Игра", "игра", "Игрушку", "игрушку", "Игрушка", "игрушка", "Майнкрафт", "майнкрафт", "Манкрафт", "манкрафт", "Манкруфт", "манкруфт"):
                if game in say:
                    toSpeak = "Я не могу включать тебе игры. Сам включай!"
                    
            for goo in ("Google", "google", "Гугл", "гугл", "Гугаль", "гугаль", "Гугол", "гугол"):
                if goo in say:
                    try:
                        toSpeak = "Открываю сайт Google"

                        open_url("https://google.com/")
                    except Exception:
                        toSpeak = "Не удалось открыть сайт Google."
                        
            for office in ("Офис", "офис", "LibreOffice", "libreoffice", "OpenOffice", "openoffice", "MicrosoftOffice", "microsoftoffice"):
                if office in say:
                    toSpeak = "Открываю офисный пакет..."
                    try:
                        subprocess.run("libreoffice")
                    except Exception:
                        subprocess.run("openoffice")
                    except Exception:
                        toSpeak = "Не удалось открыть офисный пакет"
                        
            for writer in ("Текстовый процессор", "текстовый процессор", "Текстовый редактор", "текстовый редактор", "Mousepad", "mousepad", "Kate", "kate", "KWrite", "kwrite", "Блокнот", "блокнот", "Notepad", "notepad", "Редактор текста", "редактор текста"):
                if writer in say:
                    toSpeak = "Открываю текстовый редактор..."
                    try:
                        subprocess.run(["xdg-open", "README.md"])
                    except Exception:
                        toSpeak = "Не удалось открыть текстовый редактор."
                        
            for github in ("GitHub", "Github", "github", "Гитхаб", "гитхаб"):
                if github in say:
                    toSpeak = "Открываю сайт GitHub..."
                    try:
                        open_url("https://github.com/")
                    except Exception:
                        toSpeak = "Не удалось открыть сайт GitHub."
                        
            for appStore in ("Центр программ", "центр программ", "аппстор", "апстор", "ап стор", "аппсторе", "апсторе", "ап сторе", "апп стор", "апп сторе", "эппстор", "эппсторе", "эпп стор", "эпп сторе", "эпстор", "эпсторе", "эп стор", "эп сторе", "Центр приложений", "центр приложений", "Магазин программ", "магазин программ", "Магазин приложений", "магазин приложений", "Установщик программ", "установщик программ", "Установщик приложений", "установщик приложений", "Софтвэйр", "софтвэйр", "Софтвар", "софтвар", "Софтваре", "софтваре", "Software", "software"):
                if appStore in say:
                    toSpeak = "Запускаю центр приложений..."
                    try:
                        subprocess.run("gnome-software")
                    except Exception:
                        subprocess.run("plasma-discover")
                    except Exception:
                        toSpeak = "Не удалось запустить центр приложений."
                        
            for dialapp in ("звонки", "контакты", "звонила", "звонилка", "звонилу", "звонилку", "телефон", "вызовы"):
                if dialapp in say:
                    try:
                        plyer.call.dialcall()
                    except Exception:
                        toSpeak ="Не удалось открыть приложение для звонков."
                            
            try:
                app = say.replace(i, '')
                app = app.replace(' ', '')
                for toExclude in excludeList:
                    app = app.replace(toExclude, '')
                subprocess.run(app)
                toSpeak = f"Я открыл {app}."
            except Exception:
                pass
            break
        else:
            toSpeak = ""
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak


def open_url(url):
    # Импорт Java-классов.
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Intent = autoclass("android.content.Intent")
    Uri = autoclass("android.net.Uri")

    # Создание Intent'a.
    intent = Intent()
    intent.setAction(Intent.ACTION_VIEW)

    intent.setData(Uri.parse(url))  # Установка ссылки для открытия.

    currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
    currentActivity.startActivity(intent)
