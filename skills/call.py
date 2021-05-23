from core import speak
import plyer
from jnius import autoclass

trigger = ("Позвони", "позвони", "Звони", "звони", "Звонькай", "звонькай", "Звоняй", "звоняй", "Звякни", "звякни", "Телефон", "телефон", "Звонок", "звонок") # Команды "звонка"
excludeList = ("Васисуалий", "Васисуали", "васисуалий", "васисуали", "Васян", "васян", "Васёк", "васёк", "Васися", "васися", "Васисяндра", "васисяндра", "Васька", "васька", "Вася", "вася", "Василий", "василий", "Пожалуйста", "пожалуйста")


def main(say, widget):
    for i in trigger:
        if i in say:
            num = say.replace(i, "").replace(" ", "")
            for toExclude in excludeList:
                num = num.replace(toExclude, "")
            try:
                plyer.call.makecall(num)
                toSpeak = "Звонок успешно совершён."
            except Exception:
                toSpeak = "Не удалось совершить звонок"
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
