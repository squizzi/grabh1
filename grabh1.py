#!/usr/bin/env python
from bs4 import BeautifulSoup
from time import sleep
import urllib2

text = clipboard.get_selection()
html = urllib2.urlopen(text).read()
soup = BeautifulSoup(html)
soup.prettify()
keyboard.send_key('<up>')
keyboard.send_keys(soup.h1.string)
# We need to wait a moment for the string to get pulled from url before manipulating text
sleep(1)
keyboard.send_keys('<home> <down><home> ')
