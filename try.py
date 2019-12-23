import time
import notify2

notificationMsg = {"title": "System Updater Started", "description": "The System Updater tool has been started, Wait for the another notification to install any applications. DPKG will be locked for cetrain time."}

# initialise the d-bus connection
notify2.init("News Notifier")

# create Notification object
n = notify2.Notification(None, icon="")
# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)
# set timeout for a notification
n.set_timeout(10)

for i in range(1):

    # update notification data for Notification object
    n.update(notificationMsg['title'], notificationMsg['description'])
    # show notification on screen
    n.show()

    # short delay between notifications
    time.sleep(1)

