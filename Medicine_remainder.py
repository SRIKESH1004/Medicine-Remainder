import time
from plyer import notification

while True: 
    print("Time to take Medicine")
    notification.notify(title="Its time to take Medicine",message="Take B.P tablet")
    time.sleep(5)
    notification.notify(title="Its time to take Medicine",message="Take Sugar tablet")
    time.sleep(6)