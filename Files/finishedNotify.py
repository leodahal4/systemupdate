import time
import notify2

from os import path


notificationMsg = {"title": "System Updater Installed", "description": "The System Updater tool has been sucessfully installed."}

# initialise the d-bus connection
notify2.init("News Notifier")

# create Notification object
notify = notify2.Notification(None, icon="")

# set urgency level
notify.set_urgency(notify2.URGENCY_NORMAL)
notify.set_timeout(10)

for i in range(1):
    notify.update(notificationMsg['title'], notificationMsg['description'])
    notify.show()
    time.sleep(1)
