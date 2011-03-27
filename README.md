Torn
====
Torn is a series of utilities and helper classes for the Tornado Web
project (http://www.tornadoweb.org). It is designed to create a base
project structure conforming to the VC part of MVC, and provide a few
helpful classes.

Credits
-------
The Torn project, and many of its crucial pieces, was originally
thought up by @nod (http://github.com/nod). Much of the code (torn.routes, the
settings module, etc.) are "borrowed" or inspired by his tornado_addons
project (http://github.com/nod/tornado_addons) and his default setup(s).

The torn-admin.py script, and the way it functions, is also "borrowed" 
(quite obviously) in concept from the Django project.

Requirements
------------
* Python 2.6 (the torn.route uses class decorators)
* Tornado (can be install with pip / easy_install)
* PyCurl (only necessary if you are doing asynchronous work)

Installation
------------
Simply git clone the project and run the tests with nose in the root
directory:

	nosetests

Assuming these pass, run the following to install:

	python setup.py install

(Depending on the environment, sudo may be required.)


Usage
-----
The torn project comes with a "torn-admin.py" script that should be 
installed to the bin/ of your environment. You should be able to
create a project like:

	torn-admin.py create path/to/new/project/

(The path must not exist.) To start the instance, just do:

	torn-admin.py start path/to/new/project/

...and it should start a server on the default port (which is 8080).
You can pass in parameters as well. For example, to override the port
on the command line:

	torn-admin.py start path/to/project/ -p 8081

To see the options of any command, just run:

	torn-admin.py COMMAND -h

Here are some of the options for the create command:

	Usage: torn-admin.py create [options] <project_directory>

	Options:
	  -h, --help            show this help message and exit
	  -c COOKIE_SECRET, --cookie_secret=COOKIE_SECRET
    	                    the default cookie secret
	  -a APP, --app=APP     the app module name (default 'app')
	  -p PORT, --port=PORT  the default port (default 8080)

Settings
--------
All default settings should be entered in project/app/settings.py .
However, if you need to override any of these settings, whether in a
development or production enviroment, you can create a 
project/settings_local.py file which will automatically be imported. 
This is designed so that the app/settings.py file can be under version 
control, and all mission-critical or deployment settings don't have to be.

An example project/settings_local.py should look like:

	settings = {
		"port": 8081,
		"address": "127.0.0.1",
		"secret_key": "foobarsecret"
	}

Todo
----
Torn has a lot, a LOT of potential directions. In the very short term,
we need to flesh out the torn-admin.py to see what other useful commands
it can perform. I really would like to add a form creation and validation
handler (with plug-in Javascript for client-side validation). And perhaps
one of the NoSQL databases can be supported by default (Mongo, Couch, etc.)

Contact
-------
If you use this project, we'd love to hear about it, whether it's bugs,
feature requests, etc. You can throw out an issue on GitHub if you are
having difficulty, or you can catch us at the torn mailing list:

https://groups.google.com/group/torn-python
