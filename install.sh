################################################################################
#                                                                              #
#                                                                              #
#                   System Updater Using python and Bash                       #
#                               Created by LEO                                 #
#                                                                              #
#                                                                              #
#                      Follow me on                                            #
#                      https://github.com/leodahal4                            #
#                                                                              #
#                                                                              #
################################################################################

#
# This file is responsible for starting the installation process in the textual mode.
#
# This file first checks all the necessary tools required and installs if not innstalled
# and then starts the installation process
#


finishedNotifier(){
  #Create a child python file for notifying the user that the installation is completed
  modules="import time\nimport notify2\nfrom os import path"
  title="System Updater Installed"
  description="The System Updater tool has been sucessfully installed."
  echo -e "$modules\nnotificationMsg = {'title': '$title', 'description': '$description'}\nnotify2.init('News Notifier')\nnotify = notify2.Notification(None, icon='')\nnotify.set_urgency(notify2.URGENCY_NORMAL)\nnotify.set_timeout(10)\nfor i in range(1):\n\tnotify.update(notificationMsg['title'], notificationMsg['description'])\n\tnotify.show()\n\ttime.sleep(1)" > .temp/finished
  python3 .temp/finished
}

removeTempFiles(){
  #Remove the files in the .temp folder and remove the folder too.
  rm .temp/*
  rm -r .temp
}

initialise(){
  #For Releasing Memory and creating .temp folder for using it later
  mkdir .temp
  echo -e "[+] Releasing Memory for extra efficiency [+]\n"
  sudo sync
  sudo sync && echo " "  | sudo tee /proc/sys/vm/drop_caches
  clear
}

installUpdater(){
  #Install the System Updater on the system
  clear

  #check whether Python3 is installed or not?
  tool="python3"
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            #If not then install python3
            echo -e "Python is necessary for using this tool, so continuing installation after installing Python3\n"
            echo -e "[+]\033[0;31m Python3 is not installed on your system\033[0m [+]"
            echo "[+] Updating the system for insatlling python3 [+]"
            echo ""
            sudo apt-get update #Updating System
            echo "[+] Installing Python on the system [+]"
            echo ""
            sudo apt-get install $tool #Install python3, :-   apt-get install python3
            clear
            echo "[+] Python is installed continuing installation [+]"
            sleep 2
          else
            clear
            #If python3 is installed then continue installation
            echo "[+] Python is installed continuing installation [+]"
            sleep 2
            clear
      fi
  #Remove the previous installed files(IF), which may cause trouble
  echo "[+] Removing previous files if installed [+]"
  sudo rm -r -f /etc/"updater"
  sudo rm -f /bin/update
  sleep 3
  clear
  echo "[+] Installing the files on your system [+]"
  echo ""
  echo -e "Call this updater as '\033[0;31m update \033[0m' on your terminal"
  echo ""

  #make the directory for keeping the files in /etc folder
  echo "[+] Making directory for keeping the files [+]"
  sudo mkdir /etc/"updater"
  sleep 3

  #copy all the necessary files on the /etc/updater folder
  echo "[+] Copying the files [+]"
  sudo python3 dpkg/Files/checkAndInstall.py
  sleep 4
  clear
  finishedNotifier
  removeTempFiles
  echo -e "\nSystem Updater is Installed\n\nContinue Updating using ' \033[0;31mupdate\033[0m ' command\n"
}

startInstalling(){
  #Call the necessary functions responsible for installing the tools
  initialise
  installUpdater
}

confirm(){
  #This function confirms with the user to install the software or not.
  while true; do
    #clear
    echo -e "If you want to read the Documentation then,\nPress: d\n\t'\033[0;31mq\033[0m' for Quit\n"
    echo -e "Do you want to install the software? (\033[0;31my\033[0m or \033[0;31mn\033[0m)"
    read -p "" yn
    case $yn in
      [Yy]* ) startInstalling;break;; #If user agrees to install, call the startInstalling function to start installing
      [Nn]* ) clear; echo -e "\033[0;31mAborted By User\033[0m" ;exit;;
      [Dd]* ) clear;echo -e "Press '\033[0;31mq\033[0m' to quit the Documentation\n";sleep 3; less README.md; ./install.sh;;
      [Qq]* ) clear;exit;break;;
      * ) echo "Please answer Yes(y) or No(n).";;
    esac
  done

}

#Check if the user is root or not
#If not then ask for password
if [ $UID -ne 0 ]
then
  # if not ask for password if not root
  # echo "Enter your password:"
  sudo sync
fi

#confirm the user for installing the software
confirm
