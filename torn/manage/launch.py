import sys
import os
from torn.manage.command import Command

class Launch(Command):

    name = "start"

    def setup(self):
        self.set_usage("Usage: %prog start [options] <project_directory>")

    def run(self, directory):
        sys.path.append(os.path.abspath(directory))
        import start
        start.main()
