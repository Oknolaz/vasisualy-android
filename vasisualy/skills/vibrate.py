from ..core import speak
import plyer

trigger = ("Вибратор", "вибратор", "Вибрируй", "вибрируй", "Вибрация", "вибрация", "Вибрации", "вибрации", "Вибрацию",
           "вибрацию")


def main(say, widget):
    for i in trigger:
        if i in say:
            if plyer.vibrator.exists():
                toSpeak = "Включаю вибратор на 10 секунд."
                plyer.vibrator.vibrate(time = 10)
            else:
                toSpeak = "На данном устройстве отсутствует вибратор."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
