import re
import subprocess


def updateSystem():
    # subprocess.call("apt update > update", shell=True)
    update = subprocess.check_output("apt update", shell=True)
    subprocess.call("clear", shell=True)
    print(update)
    return update


def checkUpgrades():
    updateResult = updateSystem()
    searchQuery = re.search(r"\d ['p']['a']['c']['k']['a']['g']['e']['s']", str(updateResult))
    if searchQuery is None:
        print("\n\nNo packages are to be upgraded")
    else:
        print("\n\nThere are packages to be upgraded")
        # subprocess.call("apt upgrade", shell=True)


def numberOfUpgrade():
    global updateResult
    searchNumber = "\d"
    searchQuery = searchNumber + " ['p']['a']['c']['k']['a']['g']['e']['s']"
    searchResult = re.search(r""+searchQuery+"", str(updateResult))
    packages = searchResult.group(0)
    number = int(packages[0:1])
    if number != 0:

        while searchResult is not None:
            searchNumber += "\d"
            searchQuery = searchNumber + " ['p']['a']['c']['k']['a']['g']['e']['s']"
            searchResult = re.search(r""+searchQuery+"", str(updateResult))

        else:
            print("\n\n\nWhile vitra nei gayena")
        print("\n\n"+str(searchResult.group(0))+"\nare the number of packages which are to be upgraded")
        # subprocess.call("apt upgrade --yes", shell=True)
        if searchResult is None:
            pass
    else:
        print("\n\nif ko ni else\n\nNo packages to be upgraded")
        # subprocess.call("apt update", shell=True)
