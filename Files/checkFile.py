import subprocess
from os import path
import urllib.request
def checkInternet():
    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


def removeIfInstalled():
    subprocess.call("sudo rm -r -f /etc/'updater'", shell=True)
    subprocess.call("sudo rm -f /bin/update", shell=True)



def installNotify():
    if not(path.exists("/usr/local/lib/python3.7/dist-packages/notify2.py")):
        print("Installing Notify2 module for python3 ")
        subprocess.call("pip3 install notify2", shell=True)
    else:
        pass


def check():
    installNotify()
    if path.exists("Files/toBeInstalled.py"):
        subprocess.call("echo 'if ma aayo' > yay.txt",shell=True)
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/toBeInstalled.py' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp Files/notifier.py /etc/'updater'/", shell=True)
            subprocess.call("sudo cp Files/toBeInstalled.py /etc/'updater'/", shell=True)
            return 1
        except:
            pass
    elif path.exists("systemupdate/Files/toBeInstalled.py"):
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/toBeInstalled.py' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp systemupdate/Files/notifier.py /etc/'updater'/", shell=True)
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
                subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/toBeInstalled.py' > update", shell=True)
                subprocess.call("sudo mv update /bin/", shell=True)
                subprocess.call("sudo chmod +x /bin/update", shell=True)
                subprocess.call("sudo cp systemupdate/Files/notifier.py /etc/'updater'/", shell=True)
                subprocess.call("sudo cp systemupdate/Files/toBeInstalled.py /etc/'updater'/", shell=True)
                return 1
            else:
                subprocess.call("echo 'Too Many Errors occurred\nTry connecting to the internet and try installing\nOR\nYou can copy the complete installation files and try again' > errorLogs.txt",shell=True)
                return 0
        except:
            subprocess.call("echo -e 'error in Internet\n"+print(checkInternet())+"' > yay.txt",shell=True)
            return 0

check()
