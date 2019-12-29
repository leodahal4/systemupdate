'''checkInternet
    This module checks whether the internet is connected or not using the below function
'''

import urllib.request

def check(hostAddress = "https://www.google.com"):
    '''Check(hostAddress):
        This function takes an argument to open the site provided as argument.
        If none argument is given this function takes google.com as its default argument and tries to check the internet using this default one.
    '''
    #check internet connection for downloading the repo for installation
    try:
        # Try to open the host Address and return True if connection is established
        urllib.request.urlopen(hostAddress)  # Python 3.x
        return True
    except:
        # Else return False
        return False
