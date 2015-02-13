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
* If you do not have pip it can be installed on Fedora with:
~~~
$ sudo yum -y install python-pip
~~~
* Once the dependencies are installed open autokey and select File -> New -> Script 
* Copy the script contents into the window and assign a hotkey of your choosing

### Usage 

* Select some text that begins with http:// or https:// and press the assigned hotkey(s)

##### Future Releases
Here's a few ideas I'm working on for the future:

* Add error handling that alerts the user that no header was found via lib-notify (pynotify)