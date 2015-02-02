#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2

text = clipboard.get_selection()
html = urllib2.urlopen(text).read()
soup = BeautifulSoup(html)
soup.prettify()
keyboard.send_key("<up>")
keyboard.send_keys(soup.h1.string)