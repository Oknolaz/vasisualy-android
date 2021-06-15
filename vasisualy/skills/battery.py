from ..core import speak
import plyer

trigger = ("Заряд батареи", "заряд батареи", "Заряд аккумулятора", "заряд аккумулятора", "Уровень заряда",
           "уровень заряда", "Сколько процентов зарядки", "сколько процентов зарядки", "Статус батареи",
           "статус батареи", "Статус аккумулятора", "статус аккумулятора", "Процент заряда", "процент заряда")

def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = f"Текущий заряд батареи: {str(plyer.battery.status['percentage'])}."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
