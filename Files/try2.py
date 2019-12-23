from os import path
import subprocess

if not(path.exists("/usr/local/lib/python2.7/dist-packages/notify2.py")): #or  path.exists("/usr/local/lib/python3.7/dist-packages/notify2.py")):
    print("Installing.. ")
    subprocess.call("pip install notify2",shell=True)    
else:
    print("Fuck u")
