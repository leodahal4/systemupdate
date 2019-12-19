import subprocess
import time

def continueInstallation():
    hold = "Starting the updating process"
    for i in range(9):
        if len(hold) < 32:
            hold += "."
        else:
            hold = "Starting the updating process."
        subprocess.call("clear",shell=True)
        print(hold)
        time.sleep(1)

    subprocess.call('sudo sync  | sudo tee /proc/sys/vm/drop_caches', shell= True)
    subprocess.call('clear', shell=True)

    print('\n[+] Updating system [+]\n')
    subprocess.call('sudo apt-get update',shell = True)

    subprocess.call('clear', shell = True)
    print('[+] Configuring dpkg if there are any errors [+]')
    subprocess.call('dpkg --configure -a', shell = True)

    subprocess.call('clear', shell=True)
    print('\n[+] Upgrading system [+]\n')
    subprocess.call('sudo apt-get upgrade --yes',shell = True)
    subprocess.call('sudo apt-get dist-upgrade --yes',shell = True)
    subprocess.call('sudo apt-get full-upgrade --yes',shell = True)

    subprocess.call('clear', shell=True)
    print('\n[+] Cleaning the unnecessary files downloaded [+]\n')
    subprocess.call('sudo apt autoremove --yes',shell = True)

    subprocess.call("clear", shell=True)
    print("[+] Checking If any errors occurred.[+]")
    subprocess.call("sudo apt --fix-broken install --yes", shell=True)

    subprocess.call("clear",shell=True)
    print("[+] Final touch for update [+]")
    subprocess.call("sudo apt update",shell=True)
    subprocess.call('clear',shell=True)
    print('[+] Congrats Your System Is Fully Updated Now [+]')
    print('\nContact me if you wish..\n https://github.com/leodahal4/')


if subprocess.call("$UID", shell=True) == 0:
    subprocess.call("clear",shell=True)
    continueInstallation()
else:
    print("Enter password:")
    subprocess.call("sudo sync",shell=True)
    subprocess.call("clear",shell=True)
    continueInstallation()
