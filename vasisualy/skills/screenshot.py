import plyer
from android.storage import primary_external_storage_path
from ..core import speak

trigger = ("Экран", "экран", "Скрин", "скрин", "Скриншот", "скриншот", "Фото", "фото", "Снимок", "снимок", "Фотография",
           "фотография", "Сними", "сними", "Сфотографируй", "сфотографируй", "Сфотай", "сфотай", "Сфоткай", "сфоткай",
           "Фотай", "фотай", "Фоткай", "фоткай") # Команды для создания скриншота


def main(say, widget):
    for i in trigger:
        if i in say:
            toSpeak = "Я сделал снимок экрана."
            storage = primary_external_storage_path()
            plyer.screenshot(file_path=f"{storage}/Pictures/")
            break
        else:
            toSpeak = ""
    
    if toSpeak != "":
        speak.speak(toSpeak, widget)
        
    return toSpeak
