from core import speak
import random
from jnius import autoclass
import os

trigger = ("Русская рулетка", "русская рулетка", "В русскую рулетку", "в русскую рулетку")

MediaPlayer = autoclass("android.media.MediaPlayer")
mPlayer = MediaPlayer()


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
    appDir = os.path.dirname(os.path.realpath(__file__))
    if bullet == 1:
        speak.speak("Ты выиграл.", widget)
        mPlayer.setDataSource(f'{appDir}/../assets/shot.wav')
        mPlayer.prepare()
        mPlayer.start()
        mPlayer.release()
        isRuLette = False
    else:
        speak.speak("Выстрела нет. Твоя очередь.", widget)
        mPlayer.setDataSource(f'{appDir}/../assets/misfire.wav')
        mPlayer.prepare()
        mPlayer.start()
        mPlayer.release()
    return isRuLette


def game(say, widget):
    gameState = True
    if say == "Выстрел" or say == "выстрел":
        bullet = random.choice([0, 0, 0, 0, 0, 1])
        appDir = os.path.dirname(os.path.realpath(__file__))
        if bullet == 1:
            speak.speak("Ты проиграл.", widget)
            mPlayer.setDataSource(f'{appDir}/../assets/shot.wav')
            mPlayer.prepare()
            mPlayer.start()
            mPlayer.release()
            gameState = False
        else:
            speak.speak("Кручу барабан...", widget)
            mPlayer.setDataSource(f'{appDir}/../assets/misfire.wav')
            mPlayer.prepare()
            mPlayer.start()
            mPlayer.release()
            bullet = random.choice([0, 0, 0, 0, 0, 1])
            if bullet == 1:
                speak.speak("Ты выиграл.", widget)
                mPlayer.setDataSource(f'{appDir}/../assets/shot.wav')
                mPlayer.prepare()
                mPlayer.start()
                mPlayer.release()
                gameState = False
            else:
                speak.speak("Теперь ты.", widget)
    return gameState
