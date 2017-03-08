#!/usr/bin/env python
from bs4 import BeautifulSoup
from time import sleep
from subprocess import Popen
import urllib2
import os

# Note on error handling
# Each error we handle we will 'raise' so it can be understood
# when running 'autokey-gtk -l' but we'll also send a notify-send call
# out if the user is using gnome to alert them of the error.

# FIXME: Figure out other methods of notifying user that does not rely on
# gnome calls

def notify_error(errormsg):
    # Check to see if notify-send even exists first
    if os.path.isfile('/usr/bin/notify-send'):
        # Send an error message with notify-send
        notify_send = [
            "/usr/bin/notify-send",
            "GrabH1 Autokey Script Error",
            "{}".format(errormsg)
            ]
        Popen(notify_send)
    else:
        # We'll log via print for debug, but do nothing since
        # notify-send doesn't exist
        print 'WARNING: notify-send was not found, unable to send errormsg in gui'
        pass

# Capture the clipboard selection
try:
    text = clipboard.get_selection()
except SyntaxError:
    notify_error('Could not get clipboard selection')
    raise
    exit(1)

# Try to open the text url we've grabbed, if we can't open it exit
try:
    html = urllib2.urlopen(text).read()
except urllib2.URLError, HTTPError:
    notify_error('The selected URL did not resolve and could not be read')
    raise
    exit(1)

# Prettify the url for decoding
soup = BeautifulSoup(html, "lxml")
soup.prettify()
try:
    titlestr = str(soup.title.string)
except AttributeError:
    notify_error('Unable to decode title string of selected URL')
    raise
    exit(1)

# Remove the website portion from the title if it exists
seperator = '-'
title = titlestr.split(seperator, 1)[0]

# Autokey doesnt like two strings per keyboard.send_keys() so we have to do them
# one at a time
keyboard.send_keys(title)
keyboard.send_key('<enter>')
keyboard.send_keys(text)
keyboard.send_key('<enter>')
# exit
exit(0)
