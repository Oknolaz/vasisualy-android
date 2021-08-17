import plyer
from kivymd.uix.label import MDLabel


def speak(string, widget):
    plyer.tts.speak(string)
    if len(string) > 86:
        printtext = MDLabel(
            text=string[:86],
            size_hint_x=1
        )
        widget.add_widget(printtext)
        last = 86
        while last:
            if len(string) <= last+86:
                printtext = MDLabel(
                    text=string[last:],
                    size_hint_x=1
                )
                widget.add_widget(printtext)
                last = 0
            else:
                printtext = MDLabel(
                    text=string[last:last+86],
                    size_hint_x=1
                )
                widget.add_widget(printtext)
                last += 86
    else:
        printtext = MDLabel(
            text=string,
            size_hint_x=1
        )
        widget.add_widget(printtext)

