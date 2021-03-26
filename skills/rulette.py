from core import speak
import random

trigger = ("Русская рулетка", "русская рулетка", "В русскую рулетку", "в русскую рулетку")

def isTriggered(say):
    for i in trigger:
        if i in say:
            triggered = True
            break
        else:
            triggered = False
    
    return triggered

def startGame(widget):
    bullet = random.choice([0, 0, 0, 0, 0, 1])
    isRuLette = True
    speak.speak("Я первый стреляю, если хочешь выстрелить - скажи \"выстрел\".", widget)
    if bullet == 1:
        speak.speak("Ты выиграл.", widget)
        isRuLette = False
    else:
        speak.speak("Выстрела нет. Твоя очередь.", widget)
    return isRuLette
    
def game(say, widget):
    gameState = True
    if say == "Выстрел" or say == "выстрел":
        bullet = random.choice([0, 0, 0, 0, 0, 1])
        if bullet == 1:
            speak.speak("Ты проиграл.", widget)
            gameState = False
        else:
            speak.speak("Кручу барабан...", widget)
            bullet = random.choice([0, 0, 0, 0, 0, 1])
            if bullet == 1:
                speak.speak("Ты выиграл.", widget)
                gameState = False
            else:
                speak.speak("Теперь ты.", widget)
    return gameState
