import time
import notify2

from os import path


if path.exists("/etc/updater/started"):
    notificationMsg = {"title": "System Updater Started", "description": "The System Updater tool has been started, Wait for the another notification to install any applications. DPKG will be locked for cetrain time."}
else:
    notificationMsg = {"title": "System Updater Finished", "description": "The System updating process has been finished you can now do anything you like. (^-^)"}

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

