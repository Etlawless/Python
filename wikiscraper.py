from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
import textwrap
myurl = "https://en.wikipedia.org/wiki/"
search = input("what do you want to search? ")
mysearch = myurl + search

title = 'wikiscrape\n'

path = '/users/elawless/desktop/projects/webscraper_python/wikiscrape.txt'

wikiscrape = open(path,'w')
print (mysearch)
#grabbing data
uClient = uReq(mysearch)
page_html = uClient.read()
uClient.close()
#hmtl parser
page_soup = soup(page_html, "html.parser")
#lens(containers) check result of query 
#container = containers[0]
#container.div.div.a.img["title"]


title_name = page_soup.h1.text
description = page_soup.p.text

wikiscrape.write(title_name +'\n')
print(title_name)
wikiscrape.write(description)
print ('\n'.join(textwrap.wrap(description, 16)))

quit()