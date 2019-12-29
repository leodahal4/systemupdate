import subprocess
from module import checkFile

def removeIfInstalled():
    #Remove the previous installed files(IF), which may cause trouble
    subprocess.call("sudo rm -r -f /etc/'updater'", shell=True)
    subprocess.call("sudo rm -f /bin/update", shell=True)


removeIfInstalled()
#start checking from whether the necessary files are there or not.
checkFile.check()
