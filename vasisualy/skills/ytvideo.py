from ..core import speak

trigger = ("Найди видео", "найди видео", "Поиск видео", "поиск видео", "Найти видео", "найти видео", "Включи видео",
           "включи видео", "Давай видео", "давай видео", "Ищи видео", "ищи видео") # Команды поиска видео в Youtube
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися",
               "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий",
               "Пожалуйста", "пожалуйста")

def main(say, widget):
    for i in trigger:
        if i in say:
            video_search = say.replace(i, '')
            for toExclude in excludeList:
                video_search = video_search.replace(toExclude, '')
            toSpeak = "Данная функция пока недоступна на ОС Android."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
