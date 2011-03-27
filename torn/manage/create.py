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
                        help="the default cookie secret", default=None)
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
        os.mkdir(directory)
        for base, dirs, files in os.walk(src_dir):
            base_dir = base.replace(src_dir, directory)
            for d in dirs:
                new_dir = os.path.join(base_dir, d)
                print "\tCreating directory %s" % new_dir
                os.mkdir(new_dir)
            for f in files:
                # skipping binaries
                if f.endswith('.pyc'):
                    continue
                orig_path = os.path.join(base, f)
                new_path = os.path.join(base_dir, f)
                print "\tCreating file      %s" % new_path
                shutil.copy2(orig_path, new_path)
        self._write_initial_cookie_secret(directory,
                kwargs.get('cookie_secret'))
        print "You're done!"
        print "Start the app with torn-admin.py start %s" % directory

    def _write_initial_cookie_secret(self, directory, cookie=None):
        cookie = cookie or ''.join([
            choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
            for i in range(50) ])

        settings_file = os.path.join(directory, "app", "settings.py")
        settings = open(settings_file, 'r').read()

        new_settings = re.sub(r'<COOKIE_SECRET>', cookie, settings)

        fp = open(settings_file, 'w')
        fp.write(new_settings)
        fp.close()
