import subprocess
import time
import threading
from module import checkFile

progressTimer = 0
timePassed = 0


def progress():
    global progressTimer

    if progressTimer < timePassed:
        progressTimer += 5
        subprocess.call("echo '" + str(progressTimer) + "'", shell=True)
        time = threading.Timer(1, progress)
        time.start()
    else:
        subprocess.call("echo '" + str(progressTimer) + "'", shell=True)


def removeIfInstalled():
    subprocess.call("sudo rm -r -f /etc/'updater'", shell=True)
    subprocess.call("sudo rm -f /bin/update", shell=True)


def workTODO():
    global timePassed
    subprocess.call("echo '# Getting all things ready.'", shell=True)
    timePassed = 25
    progress()
    removeIfInstalled()
    time.sleep(5)
    if checkFile.check():
        subprocess.call("echo '# Installing the updater'", shell=True)
        timePassed = 75
        progress()
        time.sleep(5)
        subprocess.call("echo '# Finishing Up'", shell=True)
        timePassed = 95
        progress()
        time.sleep(5)
        subprocess.call("echo '# Finished Installing'", shell=True)
        timePassed = 100
        time.sleep(3)
        progress()
        # subprocess.call("python3 Files/finishedNotify.py", shell=True)
        # subprocess.call("zenity --info --title 'System Updater' --text 'Installation Finished\nYou can now call the System Updater from terminal using the command\n\n\t\t'update'' --width=300 --height=300",shell=True)
    else:
        # subprocess.call("gnome-terminal -x sh -c \"echo 'Check the error logs';exec bash\"",shell=True)
        # subprocess.call("xterm -hold -e 'echo \"Check the error logs\"'",shell=True)
        subprocess.call("zenity --error --title 'System Updater' --text 'Check The Error Logs' --width=100 --height=100",shell=True)
        exit(0)
        return 0

workTODO()
