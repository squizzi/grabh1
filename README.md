# Grab H1
Autokey script which grabs the page title
~~~
<h1 class="title">My header here</h1>
~~~
of a web page and inserts it above the selected link text

### Installation
* Install `python-pip`, if you do not have `pip` it can be installed 
on Fedora with:
~~~
$ sudo yum -y install python-pip
~~~
* Run the included `setup.py` file to install the required dependencies:
~~~
# ./setup.py install
~~~
* Once the dependencies are installed open autokey and select 
File -> New -> Script 
* Copy the script contents into the window and assign a hotkey of your choosing

### Usage 

* Select some text that begins with http:// or https:// and press the assigned 
hotkey(s)

---
* **Note**: If using gnome3, the script will send any errors encountered to 
the `notify-send` utility, meaning you should receive a notification from 
the script with the error.
* If you are unable to determine what has occurred, run the script with 
`autokey-gtk -l` to see the error exceptions.
