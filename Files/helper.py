import subprocess
import time
import threading
from os import path
import urllib.request

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


def checkInternet():
    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


def installFiles():
    if path.exists("Files/toBeInstalled.py"):
        # subprocess.call("echo 'if ma aayo' > yay.txt", shell=True)
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\npython3 /etc/updater/toBeInstalled.py\n' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp Files/notifier.py /etc/updater/", shell=True)
            subprocess.call("sudo cp Files/toBeInstalled.py /etc/'updater'/", shell=True)
            return 1
        except:
            pass
    elif path.exists("systemupdate/Files/toBeInstalled.py"):
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\npython3 /etc/updater/toBeInstalled.py\n' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp systemupdate/Files/notifier.py", shell=True)
            subprocess.call("sudo cp systemupdate/Files/toBeInstalled.py /etc/'updater'/", shell=True)
            return 1
        except:
            pass
    else:
        try:
            if checkInternet():
                removeIfInstalled()
                subprocess.call("echo '# [+] Error Installing [+]'", shell=True)
                time.sleep(2)
                subprocess.call("echo '# Trying again'", shell=True)
                time.sleep(2)
                subprocess.call("echo '# Downloading from GitHub'", shell=True)
                subprocess.call("git clone 'https://github.com/leodahal4/systemupdate.git'", shell=True)
                subprocess.call("sudo mkdir /etc/'updater'", shell=True)
                subprocess.call("sudo echo -e 'clear\npython3 /etc/updater/toBeInstalled.py\n' > update", shell=True)
                subprocess.call("sudo mv update /bin/", shell=True)
                subprocess.call("sudo cp systemupdate/Files/notifier.py", shell=True)
                subprocess.call("sudo chmod +x /bin/update", shell=True)
                subprocess.call("sudo cp systemupdate/Files/toBeInstalled.py /etc/'updater'/", shell=True)
                return 1
            else:
                subprocess.call("echo 'Too Many Errors occurred\nTry connecting to the internet and try installing\nOR\nYou can copy the complete installation files and try again' > errorLogs.txt",shell=True)
                return 0
        except:
            # subprocess.call("echo -e 'error in Internet\n"+print(checkInternet())+"' > yay.txt",shell=True)
            return 0


def workTODO():
    global timePassed
    subprocess.call("echo '# Getting all things ready.'", shell=True)
    timePassed = 25
    progress()
    removeIfInstalled()
    time.sleep(5)
    if installFiles():
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
        subprocess.call("python3 Files/finishedNotify.py", shell=True)
        subprocess.call("zenity --info --title 'System Updater' --text 'Installation Finished\nYou can now call the System Updater from terminal using the command\n\n\t\t'update'' --width=300 --height=300",shell=True)
    else:
        # subprocess.call("gnome-terminal -x sh -c \"echo 'Check the error logs';exec bash\"",shell=True)
        # subprocess.call("xterm -hold -e 'echo \"Check the error logs\"'",shell=True)
        subprocess.call("zenity --error --title 'System Updater' --text 'Check The Error Logs' --width=100 --height=100",shell=True)
        return 0

def installNotify():
    if not(path.exists("/usr/local/lib/python3.7/dist-packages/notify2.py")):
        print("Installing Notify2 module for python3 ")
        subprocess.call("pip3 install notify2", shell=True)
    else:
        pass


installNotify()
workTODO()
