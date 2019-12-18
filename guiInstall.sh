#!/bin/bash
function checkZenity(){
  tool='zenity'
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            echo -e "[+]Installing other necessary tools required for installation [+]\n"
            echo -e "[+]\033[0;31m Zenity is not installed on your system\033[0m [+]\n"
            echo "[+] Updating the system for insatlling Zenity [+]"
            echo ""
            sudo apt-get update
            echo "[+] Installing Zenity on the system [+]"
            echo ""
            sudo apt-get install $tool
            clear
            echo "[+] Starting the Installer [+]"
            sleep 2
          else
            echo "[+] Starting the Installer [+]"

      fi

}
function installPython(){

  tool='python3'
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            echo "# Updating System"
            sudo apt update
            echo "50"
            echo "# Installing Python3"
            sudo apt install $tool
            echo "100"
      fi
}
checkZenity
installPython
python3 helper.py | zenity --progress --title "System Updater" --width=500 --height=500 --auto-close
#install | zenity --progress --title "System Updater" --width=500 --height=500 --auto-close
zenity --info --title "System Updater" --text "Installation Finished\nYou can now call the System Updater from terminal using the command\n\n\t\t'update'" --width=300 --height=300
clear
exit 0
