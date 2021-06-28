from ..core import speak
import sys


def old_skills_activate(user_message, widget):
    '''Активирует "старые" навыки.
    :param: user_message - сообщение пользователя (string)
    :param: widget - виджет, в который должно выводиться сообщение навыка (QWidget)
    '''
    skills = ("time_date", "exit", "weather", "music", "open", "screenshot", "search", "poweroff",
              "ytvideo", "resay", "wiki", "location", "weather_no_city", "translate", "news", "coin",
              "shoplist", "todolist", "netconnection", "math", "crystal_ball",
              "random_num", "timer", "brightness", "battery", "vibrate", "call")

    skillUse = False
    skill_loc = "vasisualy.skills."

    for skill in skills:
        skill = skill_loc + skill
        if (skill == skill_loc + "time_date"):
            if sys.modules[skill].main(user_message):
                speak.speak(sys.modules[skill].main(user_message), widget)
                skillUse = True
                break

        if skill == skill_loc + "math":
            if sys.modules[skill].calculate(user_message, widget):
                skillUse = True
                break

        if ((not skillUse) and (skill != skill_loc + "time_date")
                and (skill != skill_loc + "math")):
            if sys.modules[skill].main(user_message, widget):
                skillUse = True
                break

    return skillUse
