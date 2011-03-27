import sys
import os
from torn.manage.command import Command
from torn.util import PARSER

class Launch(Command):

    name = "start"

    def setup(self):
        # Just using the default torn startup parser
        self.parser = PARSER
        self.set_usage("Usage: %prog start [options] <project_directory>")

    def run(self, directory, *args, **kwargs):
        sys.path.append(os.path.abspath(directory))
        try:
            import start
        except ImportError:
            self.parser.print_usage()
            sys.exit()
        start.main()
