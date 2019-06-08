from bs4 import BeautifulSoup
import mechanize
import time
import urllib
import string

start = input("Where would you like to start searching?\n")
br = mechanize.Browser()
r = br.open(start)
html = r.read()

soup = BeautifulSoup(html)
for link in soup.find_all('a'):
    print (link.get('href'))