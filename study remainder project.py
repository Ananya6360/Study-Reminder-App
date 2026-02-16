import time
import pyttsx3
import playsound
from plyer import notification

engine = pyttsx3.init()


reminder_times = ["11:25 pM", "07:17 AM"]

shown_reminders = []

while True:
    current_time = time.strftime("%I:%M %p")
    print("Current Time:", current_time)

    if current_time in reminder_times and current_time not in shown_reminders:
        notification.notify(
            title="⏰ Study Reminder!",
            message=f"It's {current_time}, Anu! Stop scrolling  reels 😅 and go study 📚✨",
            timeout=10
        )

        engine.say(f"Anu, it's {current_time}. Time to study now.")
        engine.runAndWait()

        shown_reminders.append(current_time)
        time.sleep(60) this code is working chati 
