import os
#from core import speak
import time

trigger = ("Поставь таймер", "поставь таймер", "Включи таймер", "включи таймер")

def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = "Таймер включен."
            break
        else:
            toSpeak = ""
            
    if toSpeak != "":
        print(toSpeak)
    return toSpeak

def timer(sleep):
    time.sleep(sleep)
    print("Время вышло!")
    
if __name__ == "__main__":
    timer(20)
