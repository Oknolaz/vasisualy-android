from core import speak
import random
import time

trigger = ("Пока", "пока", "Прощай", "прощай", "До свидания", "до свидания", "Прощайте", "прощайте", "Удачи", "удачи", "Бывай", "бывай", "До встречи", "до встречи", "Увидимся", "увидимся", "Выход", "выход", "Exit", "exit")

def main(say):
    for i in trigger:
        if i == say:
            bye = random.choice(("Пока, мой друг.", "Пока, товарищ.", "До встречи.", "Прощай.", "До свидания.", "Не покидай меня!", "Очень жаль расставаться с тобой."))
            speak.speak(bye)
            time.sleep(5)
            exit()
            
    return ""