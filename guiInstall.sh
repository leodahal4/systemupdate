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
#This file is responsible for gui installation process for the tool
#
#This file checks whether all the necessary tools required are installed or not
#and if not then installs the necessary tools and starts the gui installation process
#

#check if Zenity is installed on the system or not
function checkZenity(){
  tool='zenity'
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            #install Zenity
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
            #if Zenity is installed start the installation process
            echo "[+] Starting the Installer [+]"

      fi

}


makeTemp(){
    #make a temp folder for keeping the temporary needed files
    mkdir .temp
}

removeTemp(){
    #remove the files in the temp directory and remove the folder too.
    rm .temp/*
    rm -r .temp
}

finishedNotifier(){
  #Create a child python file for notifying the user that the installation is completed
  modules="import time\nimport notify2\nfrom os import path"
  title="System Updater Installed"
  description="The System Updater tool has been sucessfully installed. You can now use this tool using update command."
  echo -e "$modules\nnotificationMsg = {'title': '$title', 'description': '$description'}\nnotify2.init('News Notifier')\nnotify = notify2.Notification(None, icon='')\nnotify.set_urgency(notify2.URGENCY_NORMAL)\nnotify.set_timeout(100)\nfor i in range(1):\n\tnotify.update(notificationMsg['title'], notificationMsg['description'])\n\tnotify.show()\n\ttime.sleep(1)" > .temp/finished
  python3 .temp/finished
}

#check if python3 is installed on the system or not
function checkPython(){
  tool='python3'
  dpkg -s $tool &> /dev/null
      if [ $? -ne 0 ]
          then
            #install python3
            echo "# Updating System"
            sudo apt update
            echo "50"
            echo "# Installing Python3"
            sudo apt install $tool #apt-get install python3
            echo "100"
      fi
}

#check if user is root or not
if [ $UID -ne 0 ]
then
  #if not ask for password
  # echo "Enter your password:"
  sudo sync
fi

initialize(){
    makeTemp
  #start the installation
    checkZenity
    checkPython
    sleep 2
    clear
}

#confirm for installing the software
zenity --question --width 300 --title 'System Updater' --text 'Do you want to install this software on your system?'

if [ $? -eq 0 ]
then
    initialize
    #call the helper file for installing the software
    python3 Files/helper.py | zenity --progress --title "System Updater" --width=500 --height=500 --auto-close
    finishedNotifier
    #clear
    removeTemp
    exit 0
fi

#user disagreed for installation
echo -e "Aborted By User\n\n"
exit 0
