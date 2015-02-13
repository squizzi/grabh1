#!/usr/bin/env python
from bs4 import BeautifulSoup
from time import sleep
import urllib2

text = clipboard.get_selection()
html = urllib2.urlopen(text).read()
soup = BeautifulSoup(html)
soup.prettify()
# Autokey doesn't like two strings per keyboard.send_keys() so we have to do them one at a time
keyboard.send_keys(soup.h1.string)
keyboard.send_key('<enter>') 
keyboard.send_keys(text) 
keyboard.send_keys('<enter>')
# 1 space indention (optional, comment out if not desired)
# We need to wait a moment for the string to get pulled from url before manipulating text
sleep(1.5)
keyboard.send_keys('<up><up><home> <up><home> ')
# Return to new line
keyboard.send_keys('<down><down>')