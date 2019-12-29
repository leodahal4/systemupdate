import subprocess
from os import path
import urllib.request
from module import checkInternet


def removeIfInstalled():
    #Remove the previous installed files(IF), which may cause trouble
    subprocess.call("sudo rm -r -f /etc/'updater'", shell=True)
    subprocess.call("sudo rm -f /bin/update", shell=True)


def installNotify():

    #install the notify2 module on the system for notificating the user
    if not(path.exists("/usr/local/lib/python3.7/dist-packages/notify2.py")):
        print("Installing Notify2 module for python3 ")
        subprocess.call("pip3 install notify2", shell=True)
    else:
        pass


def check():
    installNotify() # install notify2 first

    #check if there is the file to be installed or not

    #check on the normal directory
    if path.exists("Files/toBeInstalled.py") and path.exists("Files/notifier.py"):
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/toBeInstalled.py' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp Files/notifier.py /etc/'updater'/", shell=True)
            subprocess.call("sudo cp Files/updateUninstall /bin/", shell=True)
            subprocess.call("sudo cp Files/toBeInstalled.py /etc/'updater'/", shell=True)
            return 1
        except:
            pass
    #check if already git repo is downloaded
    elif path.exists("systemupdate/Files/toBeInstalled.py") and path.exists("systemupdate/Files/notifier.py"):
        try:
            removeIfInstalled()
            subprocess.call("sudo mkdir /etc/'updater'", shell=True)
            subprocess.call("sudo echo -e 'clear\n python3 /etc/updater/toBeInstalled.py' > update", shell=True)
            subprocess.call("sudo mv update /bin/", shell=True)
            subprocess.call("sudo chmod +x /bin/update", shell=True)
            subprocess.call("sudo cp systemupdate/Files/notifier.py /etc/'updater'/", shell=True)
            subprocess.call("sudo cp systemupdate/Files/updateUninstall /bin/", shell=True)
            subprocess.call("sudo cp systemupdate/Files/toBeInstalled.py /etc/'updater'/", shell=True)
            return 1
        except:
            pass
    #download the repo and start installation using the files downloaded from the repo
    else:
        try:
            #check internet connection for downloading
            conn = checkInternet.check('github.com')
            if conn:
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
                subprocess.call("sudo cp systemupdate/Files/updateUninstall /bin/", shell=True)
                subprocess.call("sudo cp systemupdate/Files/toBeInstalled.py /etc/'updater'/", shell=True)
                return 1
            else:
                subprocess.call("echo 'Too Many Errors occurred\nTry connecting to the internet and try installing\nOR\nYou can copy the complete installation files and try again' > errorLogs.txt",shell=True)
                return 0
        except:
            subprocess.call("echo -e 'error in Internet\n"+print(checkInternet())+"' > yay.txt",shell=True)
            return 0

#start checking from whether the necessary files are there or not.
check()
