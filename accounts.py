import sys
import time
import getopt
import simplejson
from selenium import webdriver
from SeleniumHelper import SeleniumHelper

class TwitterCreator(SeleniumHelper):
    # ... Existing code ...

    def desktopCreateMultipleUsers(self, email, usernames):
        self.loadPage(self.DESKTOP_URL_CREATE)
        self.waitAndWrite(self.DESKTOP_FIELD_SIGN_UP_EMAIL, email)
        self.submitForm(self.selectAndWrite(self.DESKTOP_FIELD_SIGN_UP_PASSWORD, row['wachabangi']))
        
        for username in usernames:
            self.waitShowElement(self.DESKTOP_PAGE_CONTAINER)
            self.loadPage(self.DESKTOP_URL_SKIP)
            self.submitForm(self.waitAndWrite(self.DESKTOP_FIELD_SIGN_UP_USERNAME, username))
            self.waitShowElement(self.DESKTOP_PAGE_CONTAINER)
            self.loadPage(self.DESKTOP_URL_MAIN)
            time.sleep(5)  # Adjust the delay as needed

    # ... Existing code ...

def main(argv):
    # ... Existing code ...
    
    inputFile = None  # Initialize inputFile variable
    
    while not inputFile:
        inputFile = input('Input file path: C:\\Users\\User\\OneDrive\\Documents\\twitter.json')
        
    # Rest of the code remains the same

    try:
        data = simplejson.loads(open(inputFile).read())
        email = data['email']
        usernames = data['usernames']
    except:
        print('Invalid input file format')
        return

    creator = TwitterCreator()
    print('Process started')
    creator.desktopCreateMultipleUsers(email, usernames)
    print('Process ended')

# ... Existing code ...

if __name__ == "__main__":
    main(sys.argv[1:])
