import re
import subprocess


def try():
    subprocess.call("apt update > update", shell=True)


sentence = "10 packages can be upgraded. Run 'apt list --upgradable' to see them."
ownreal = "All packages are up to date."
search = re.search(r'\A\d',ownreal)

if search is None:
    print("No packages are to be upgraded")
    subprocess.call("apt update", shell=True)
else:
    if int(search[0]) > 0:
        print("There are packages which are to be upgraded")
        subprocess.call("apt upgrade --yes", shell=True)
    else:
        print("No packages to be upgraded")
        subprocess.call("apt update", shell=True)

