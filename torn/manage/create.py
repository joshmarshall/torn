import os
import shutil
import re
from random import choice
from torn.manage.command import Command

class ProjectAlreadyExists(Exception):
    pass

class Create(Command):

    name = "create"

    def setup(self):
        self.add_option("-c", "--cookie_secret", dest="cookie_secret",
                        help="the default cookie secret",
                        default=self._get_cookie_secret())
        self.add_option("-a", "--app", dest="app",
                        help="the app module name (default 'app')",
                        default="app")
        self.add_option("-p", "--port", dest="port",
                        help="the default port (default 8080)",
                        type="int", default=8080)
        self.set_usage("Usage: %prog create [options] <project_directory>")

    def run(self, directory, **kwargs):
        while directory.endswith('/'):
            directory = directory[:-1]
        src_dir = os.path.join(os.path.dirname(__file__), "structure")
        if os.path.exists(directory):
            raise ProjectAlreadyExists()
        print "Populating directory %s" % directory
        default_app_dir = os.path.join(src_dir, "app")
        new_app_dir = os.path.join(directory, kwargs.get("app"))
        os.makedirs(directory)
        kwargs.setdefault("base", os.path.basename(directory))
        for base, dirs, files in os.walk(src_dir):
            # Overwriting base app directory with
            # custom app directory
            if base.startswith(default_app_dir):
                base_dir = base.replace(default_app_dir, new_app_dir)
            else:
                base_dir = base.replace(src_dir, directory)

            for d in dirs:
                new_dir = os.path.join(base_dir, d)
                print "\tCreating directory %s" % new_dir
                os.makedirs(new_dir)
            for f in files:
                # skipping python binaries
                if f.endswith('.pyc'):
                    continue
                orig_path = os.path.join(base, f)
                new_path = os.path.join(base_dir, f)
                print "\tCreating file      %s" % new_path
                if f.endswith('.py') or f.endswith('.htm') or \
                    f.endswith('.html'):
                    # if it's a python or html file, do string
                    # replacements as necessary
                    stat = os.stat(orig_path)
                    orig_fp = open(orig_path, "r")
                    new_fp = open(new_path, "w")
                    data = orig_fp.read()
                    for key, val in kwargs.iteritems():
                        data = data.replace("<%s>" % key.upper(), str(val))
                    new_fp.write(data)
                    orig_fp.close()
                    new_fp.close()
                else:
                    shutil.copy2(orig_path, new_path)

        print "You're done!"
        print "Start the app with torn-admin.py start %s" % directory

    def _get_cookie_secret(self):
        """ Generates default cookie secret """
        choices = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        return ''.join([choice(choices) for i in range(50)])
