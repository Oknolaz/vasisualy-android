from core import speak

poweroff = ("Выключи пк", "выключи пк", "Выключи ПК", "выключи ПК", "Выключи компьютер", "выключи компьютер", "Выключи телефон", "выключи телефон", "Выключить телефон", "выключить телефон") # Команды выключения пк
reboot = ("Перезагрузи пк", "перезагрузи пк", "Перезагрузи ПК", "перезагрузи ПК", "Перезагрузи компьютер", "перезагрузи компьютер", "Перезагрузка", "перезагрузка", "Перезагрузи телефон", "перезагрузи телефон", "Перезагрузка телефона", "перезагрузка телефона") # Команды перезагрузки пк

def main(say, widget):
    for i in poweroff:
        if i in say:
            toSpeak = "Данная функция пока недоступна на ОС Android."
        
    for i in reboot:
        if i in say:
            toSpeak = "Данная функция пока недоступна на ОС Android."
        else:
            toSpeak = ""
            
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
