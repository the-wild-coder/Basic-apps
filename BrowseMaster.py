#!usr/bin/env python3

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import time
import sys

"""
BrowseMaster is more
of a web content 
viever than a browser.

It uses urllib to get the HTML
from the site and BeautifulSoup
to get the text that is in the site.
"""

class highlights:
        # highligt colors
        BLUE = '\033[94m'
        OK = '\033[92m'
        ERROR = '\033[91m'
        WARNING = '\033[93m'
        RESET = '\033[0m'


os = sys.platform
print(highlights.BLUE + 'BrowseMaster' + highlights.RESET + '\n currently running on ' + os + '\n')

print(highlights.WARNING + 'Please note: \n You cannot interact with the sites those you open. \n'
      + highlights.RESET)
while True:
        try:
                url = input(highlights.BLUE + '\n enter address \n > ' + highlights.RESET)
                print('Loading website...')
                with open('BrowseHistory.txt', 'a') as file:
                        file.write(url + '\n')
                        
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, features='html.parser')
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split('  '))
                text = '\n'.join(chunk for chunk in chunks if chunk)
                print(highlights.OK + 'Done! \n' + highlights.RESET)
                time.sleep(0.5)
        except ValueError:
                
                print(highlights.ERROR + '\u2a2f  Error: \n Invalid URL.' + highlights.RESET)
                continue
        except urllib.error.URLError:
                
                print(highlights.ERROR + '\u2a2f  Error: \n Could not open that site.' + highlights.RESET)
                continue

        print(text)
        
        for script in soup(['script', 'style']):
                script.extract()



        
    

