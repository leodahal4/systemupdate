clear


echo "[+] Provide your password and sit back [+]"
sudo sync
clear
echo -e "[+] Releasing Memory for extra efficiency [+]\n"
sudo sync
sudo sync && echo " "  | sudo tee /proc/sys/vm/drop_caches

clear

echo "[+] Removing previous files if installed [+]"
sudo rm -r -f /etc/"updater"
sudo rm -f /bin/update

sleep 3

clear
echo "[+] Installing the files on your system [+]"

echo ""
echo -e "Call this updater as '\033[0;31m update \033[0m' on your terminal"

echo ""
echo "[+] Making directory for keeping the files [+]"
sudo mkdir /etc/"updater"

sleep 2
echo "[+] Copying the files [+]"

fileText="clear \n echo 'Please wait calling the system functions'\n echo 'Sit back man. '\n echo 'Get on your own work'\n sleep 5\n clear\n python3 /etc/'System Updater files'/*.py"
sudo echo -e $fileText > update

sudo mv update /bin/
sudo chmod +x /bin/update
sudo cp main.py /etc/"update"/

sleep 3
clear

tool="python3"
dpkg -s $tool &> /dev/null

    if [ $? -ne 0 ]

        then
          echo -e "[+]\033[0;31m Python3 is not installed on your system\033[0m [+]"
          echo "[+] Updating the system for insatlling python3 [+]"

          echo ""

          sudo apt-get update

          echo "[+] Installing Python on the system [+]"

          echo ""
          sudo apt-get install $tool
          echo "[+] Python is installed continuing installation [+]"
        else
            echo "[+] Python is installed continuing installation [+]"
    fi
update
