from lxml import html
import requests

source = requests.get('https://httpstatuses.com/')
Html = html.fromstring(source.content)
Html_file= open("test1.py","w")
Html_file.write(str(Html))
Html_file.close()
with open("test1.py","r") as file:
    var = file.read()

import urllib2
from BeautifulSoup import BeautifulSoup

sc = urllib2.urlopen('https://httpstatuses.com/')
soup = BeautifulSoup(sc)

text = soup.body.find('li').text