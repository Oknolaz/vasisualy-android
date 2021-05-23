import plyer
from kivymd.uix.label import MDLabel


def speak(string, widget):
    plyer.tts.speak(string)
    printtext = MDLabel(text=string)
    widget.add_widget(printtext)
