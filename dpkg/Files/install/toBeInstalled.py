import subprocess
import time
from module import checkUpgrade
from module import checkInternet


def aptFunc(command):
    subprocess.call('sudo apt '+ command +' --yes', shell=True)

def finish():
    # Again just some extra...
    print('[+] Congrats Your System Is Fully Updated Now [+]')
    print('\nContact me if you wish..\n https://github.com/leodahal4/')


def continueUpdating():
    """ContinueUpdating
        This function is responsible for updating and upgrading the system
    """

    # create a started file for notifying the user that the System updating process has started
    subprocess.call("echo "" > /etc/updater/started", shell=True)
    subprocess.call("python3 /etc/updater/notifier.py", shell=True)
    time.sleep(2)

    # actually start updating now.
    # just some extra.....
    hold = "Starting the updating process"
    conn = checkInternet.check()
    for i in range(9):
        if len(hold) < 32:
            hold += "."
        else:
            if conn:
                pass
            else:
                subprocess.call('clear', shell=True)
                print("[+] No internet connection [+]")
                exit(0)
            hold = "Starting the updating process."
        subprocess.call("clear", shell=True)
        print(hold)
        time.sleep(1)

    # release memory for starting the updating the process
    subprocess.call('sudo sync  | sudo tee /proc/sys/vm/drop_caches', shell=True)
    subprocess.call('clear', shell=True)

    # update the system
    print('\n[+] Updating system [+]\n')
    updateResult = subprocess.check_output('sudo apt update', shell=True)

    if checkUpgrade.checkUpgrades(updateResult):
        print("\n[+] No packages are to be upgraded [+]\n")
        # reconsigure the dpkg if there were any errors
        subprocess.call('clear', shell=True)
        print('[+] Configuring dpkg if there are any errors [+]')
        subprocess.call('sudo dpkg --configure -a', shell=True)

    else:
        # reconsigure the dpkg if there were any errors
        subprocess.call('clear', shell=True)
        print('[+] Configuring dpkg if there are any errors [+]')
        subprocess.call('sudo dpkg --configure -a', shell=True)

        # upgrade the system
        subprocess.call('clear', shell=True)
        print('\n[+] Upgrading system [+]\n')
        aptFunc('upgrade')
        aptFunc('dist-upgrade')
        aptFunc('full-upgrade')

        # remove the unnecessary files downloaded while upgrading
        subprocess.call('clear', shell=True)
        print('\n[+] Cleaning the unnecessary files downloaded [+]\n')
        aptFunc('autoremove')

        # fix any errors if occured
        subprocess.call("clear", shell=True)
        print("[+] Checking If any errors occurred.[+]")
        aptFunc('--fix-broken install')

        # final touch for update
        subprocess.call("clear", shell=True)
        print("[+] Final touch for update [+]")
        subprocess.call("sudo apt update", shell=True)
        subprocess.call('clear', shell=True)

    # call the notifier for notifying the user that the process has been finished
    subprocess.call("rm /etc/updater/started", shell=True)
    subprocess.call("python3 /etc/updater/notifier.py", shell=True)

    finish()

# check if the user is root
if subprocess.call("$UID", shell=True) == 0:
    # if yes then clear the screen and start the process
    subprocess.call("clear", shell=True)
    continueUpdating()
else:

    # if not then ask for password to the user and start the process
    print("Enter password:")
    subprocess.call("sudo sync", shell=True)
    subprocess.call("clear", shell=True)
    continueUpdating()
