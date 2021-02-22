from core import speak
import plyer

increase = ("Добавь яркости", "добавь яркости", "Увеличь яркость", "увеличь яркость", "Добавить яркости", "добавить яркости", "Увеличить яркость", "увеличить яркость", "Усиль яркость", "усиль яркость", "Усилить яркость", "усилить яркость")
decrease = ("Уменьши яркость", "уменьши яркость", "Убавь яркость", "убавь яркость", "Уменьшить яркость", "уменьшить яркость", "Убавить яркость", "убавить яркость", "Меньше яркости", "меньше яркости", "Минимум яркости", "минимум яркости")

def main(say, widget):
    for i in increase:
        if i in say:
            curBright = plyer.brightness.current_level()
            if curBright == 100:
                toSpeak = "Яркость экрана равна ста процентам. Ярче сделать не получится."
            elif curBright > 90:
                plyer.brightness.set_level(100)
                toSpeak = "Яркость увеличена до максимального уровня."
            else:
                plyer.brightness.set_level(curBright + 10)
                toSpeak = "Яркость экрана увеличена на 10 процентов."
            break
        else:
            toSpeak = ""
            
    for i in decrease:
        if i in say:
            curBright = plyer.brightness.current_level()
            if curBright == 1:
                toSpeak = "Яркость экрана равна одному проценту. Меньше сделать не получится."
            elif curBright < 10:
                plyer.brightness.set_level(1)
                toSpeak = "Яркость уменьшена до предела."
            else:
                plyer.brightness.set_level(curBright + 10)
                toSpeak = "Яркость экрана уменьшена на 10 процентов."
            break
        
    if toSpeak != "":
        speak.speak(toSpeak, widget)
    return toSpeak
