import time
from winotify import Notification,audio
toast= Notification(
            app_id="reminder",
            title="please drink water now!",
            msg="Drinking enough water offers health benefits, however, drinking too much water, "
                    "such as 3-4 liters of water, in a short period leads to water intoxication."
                    " For proper metabolism, a normal human body requires about two liters of water.",
            duration="short",

            icon=r"C:\Users\hp\PycharmProjects\myproject\water.png")
toast.set_audio(audio.SMS,loop=True)
while True:
    toast.show()
    time.sleep(60*60)