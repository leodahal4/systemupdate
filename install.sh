installUpdater(){
  clear
  echo -e "[+] Releasing Memory for extra efficiency [+]\n"
  sudo sync
  sudo sync && echo " "  | sudo tee /proc/sys/vm/drop_caches
  clear
  tool="python3"
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            echo -e "Python is necessary for using this tool, so continuing installation after installing Python3\n"
            echo -e "[+]\033[0;31m Python3 is not installed on your system\033[0m [+]"
            echo "[+] Updating the system for insatlling python3 [+]"
            echo ""
            sudo apt-get update
            echo "[+] Installing Python on the system [+]"
            echo ""
            sudo apt-get install $tool
            clear
            echo "[+] Python is installed continuing installation [+]"
            sleep 2
          else
            clear
            echo "[+] Python is installed continuing installation [+]"
            sleep 2
            clear
            #echo -e "\nSystem Updater is Installed\n\nContinue Updating using ' \033[0;31mupdate\033[0m ' command"
      fi
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
  sleep 3
  echo "[+] Copying the files [+]"
  fileText="clear\n python3 /etc/updater/*.py"
  sudo echo -e $fileText > update
  sudo mv update /bin/
  sudo chmod +x /bin/update
  # sudo cp Files/uninstaller.sh /etc/updater/
  sudo python3 Files/checkFile.py
  sleep 4
  clear
  python3 Files/finishedNotify.py
  echo -e "\nSystem Updater is Installed\n\nContinue Updating using ' \033[0;31mupdate\033[0m ' command\n"
}

if [ $UID -ne 0 ]
then
  echo "Enter your password:"
  sudo sync
fi

while true; do
  clear
  echo -e "If you want to read the Documentation then,\nPress: d\n\t'\033[0;31mq\033[0m' for Quit\n"
  echo -e "Do you want to install the software? (\033[0;31my\033[0m or \033[0;31mn\033[0m)"
  read -p "" yn
  case $yn in
    [Yy]* ) installUpdater;break;;
    [Nn]* ) clear; echo -e "\033[0;31mAborted By User\033[0m" ;exit;;
    [Dd]* ) clear;echo -e "Press '\033[0;31mq\033[0m' to quit the Documentation\n";sleep 3; less README.md; ./install.sh;;
    [Qq]* ) clear;exit;break;;
    * ) echo "Please answer Yes(y) or No(n).";;
  esac
done
