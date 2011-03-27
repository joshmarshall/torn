import os
import shutil
import re
import tarfile
from random import choice
from torn.manage.command import Command

class ProjectAlreadyExists(Exception):
    pass

class Create(Command):

    name = "create"

    def setup(self):

        default_tar_path = os.path.join(os.path.dirname(__file__),
                                        "../structure.tar.gz")

        self.add_option("-c", "--cookie_secret", dest="cookie_secret",
                        help="the default cookie secret",
                        default=self._get_cookie_secret())
        self.add_option("-a", "--app", dest="app",
                        help="the app module name (default 'app')",
                        default="app")
        self.add_option("-p", "--port", dest="port",
                        help="the default port (default 8080)",
                        type="int", default=8080)
        self.add_option("-t", "--template", dest="template",
                        help="the path to a custom template (tar.gz)",
                        metavar="FILE", default=default_tar_path)
        self.set_usage("Usage: %prog create [options] <project_directory>")

    def run(self, directory, **kwargs):
        while directory.endswith('/'):
            directory = directory[:-1]

        tar_path = kwargs.get("template")
        if not tar_path or not os.path.exists(tar_path):
            raise Exception("Structure tar is missing!")
        # currently hardcoded to tar.gz right now
        tar = tarfile.open(tar_path, mode="r:gz")

        if os.path.exists(directory):
            raise ProjectAlreadyExists()
        print "Populating directory %s" % directory

        # Because it's in a tarfile, this SHOULD be the base path
        src_dir = "torn/data/structure"
        default_app_dir = os.path.join(src_dir, "app")
        new_app_dir = os.path.join(directory, kwargs.get("app"))

        os.makedirs(directory)
        kwargs.setdefault("base", os.path.basename(directory))

        for tarinfo in tar:
            # Overwriting base app directory with
            # custom app directory
            path = tarinfo.name.replace(src_dir, directory)
            if path == directory:
                # Root structure dir
                continue
            if tarinfo.name.startswith(default_app_dir):
                # app/ paths get special treatment
                path = tarinfo.name.replace(default_app_dir, new_app_dir)

            if tarinfo.isdir():
                print "\tCreating directory %s" % path
                os.makedirs(path)
                continue

            # skipping python binaries
            if path.endswith('.pyc'):
                continue
            print "\tCreating file      %s" % path
            orig_fp = tar.extractfile(tarinfo)
            data = orig_fp.read()

            if path.endswith('.py') or path.endswith('.htm') or \
                path.endswith('.html'):
                # if it's a python or html file, do string
                # replacements as necessary
                new_fp = open(path, "w")
                new_fp.write(replace_text(data, kwargs))
                new_fp.close()
            else:
                new_fp = open(path, "wb")
                new_fp.write(data)
                new_fp.close()

        print "You're done!"
        print "Start the app with torn-admin.py start %s" % directory

    def _get_cookie_secret(self):
        """ Generates default cookie secret """
        choices = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        return ''.join([choice(choices) for i in range(50)])

def replace_text(data, replacement):
    for key, val in replacement.iteritems():
        data = data.replace("<%s>" % key.upper(), str(val))
    return data
