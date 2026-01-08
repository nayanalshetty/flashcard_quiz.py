import time
from datetime import datetime
import winsound

print("===== PYTHON ALARM CLOCK WITH SOUND =====")

alarm_time = input("Enter alarm time (HH:MM:SS) in 24-hour format: ")

print("Alarm set for:", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

    if current_time == alarm_time:
        print("⏰⏰⏰ WAKE UP! ALARM RINGING! ⏰⏰⏰")

        # Play sound 5 times
        for i in range(5):
            winsound.Beep(1000, 1000)  # (frequency, duration in ms)

        break

    time.sleep(1)
