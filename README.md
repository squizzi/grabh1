# grabh1
Autokey script which grabs the header text 
~~~
<h1>My header here</h1>
~~~
of a web page and inserts it above the selected link text

### Installation
* grabh1 requires BeautifulSoup4 to function, you can install that with
~~~
$ sudo pip install beautifulsoup4
~~~
* Once the dependencies are installed open autokey and select File -> New -> Script 
* Copy the script contents into the window and assign a hotkey of your choosing

### Usage 

* Select some text that begins with http:// or https:// and press the assigned hotkey(s)

##### Caveats
* The ```keyboard.send_key()``` function is called prior to printing the string via ```keyboard.send_keys()```.  Meaning that if the script is used at the top of a text box both the text and link will reside on the same line.  This will be fixed in a future release.

##### Future Releases
Here's a few ideas I'm working on for the future:

* Add error handling that alerts the user that no header was found via lib-notify (pynotify)

