import plyer
from kivymd.uix.label import MDLabel
from kivy.properties import ListProperty


class Message(MDLabel):
    background_color = ListProperty()

    def __init__(self, *args, **kwargs):
        MDLabel.__init__(self, *args, **kwargs)
        self.text_size = self.size
        self.size = self.texture_size


def speak(string, widget):
    plyer.tts.speak(string)
    printtext = Message(text=string)
    widget.add_widget(printtext)
