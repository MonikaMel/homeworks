#import urllib.request
#source = urllib.request.urlopen("c")
#html = source.read()
#with open('test1.html' , 'w') as  file:
 #   file.write(html)
#print('The End')

from lxml import html
import requests
source = requests.get('https://httpstatuses.com/')
Html = html.fromstring(source.content)
Html_file= open("test1.py","w")
Html_file.write(str(Html))
Html_file.close()
print('End')