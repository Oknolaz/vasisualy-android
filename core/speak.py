import plyer
from kivymd.uix.label import MDLabel


def speak(string, widget):
    plyer.tts.speak(string)
    printtext = MDLabel(text = string, size_hint_y = None, text_size = [widget.width, None])
    widget.add_widget(printtext)
