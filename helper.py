import subprocess
import time
import threading

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


def installFiles():
    try:
        subprocess.call("sudo mkdir /etc/'updater'", shell=True)
        subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/*.py' > update", shell=True)
        subprocess.call("sudo mv update /bin/", shell=True)
        subprocess.call("sudo chmod +x /bin/update", shell=True)
        subprocess.call("sudo cp toBeInstalled.py /etc/'updater'/", shell=True)
    except FileNotFoundError:
        try:
            subprocess.call("echo '[+] Error Installing [+]'", shell=True)
            subprocess.call("Trying again..", shell=True)
            subprocess.call("git clone 'https://github.com/leodahal4/systemupdate.git'", shell=True)
            subprocess.call("sudo cp systemupdate/toBeInstalled.py /etc/'updater'/", shell=True)
        except:
            print("[+] Too many errors [+]")
            exit(0)


def workTODO():
    global timePassed
    subprocess.call("echo '# Getting all things ready.'", shell=True)
    timePassed = 25
    progress()
    removeIfInstalled()
    time.sleep(5)
    subprocess.call("echo '# Installing the updater'", shell=True)
    timePassed = 75
    progress()
    installFiles()
    time.sleep(5)
    subprocess.call("echo '# Finishing Up'", shell=True)
    timePassed = 90
    progress()
    time.sleep(5)
    subprocess.call("echo '# Finished Installing'", shell=True)
    timePassed = 100
    progress()


workTODO()
