""" The basic command class, which each command should
subclass.
"""

import optparse
import sys

class Command(object):
    """ The root command class. Should be subclassed. """

    name = None

    def __init__(self):
        self.parser = optparse.OptionParser()
        self.setup()

    def setup(self):
        """ This method should be overwritten in
        the subclasses to add arguments to the parser.
        """
        pass

    def add_option(self, *args, **kwargs):
        """ Just a wrapper for the parser.add_option method. """
        self.parser.add_option(*args, **kwargs)

    def set_usage(self, *args, **kwargs):
        """ Just a wrapper for the parser.set_usage method. """
        self.parser.set_usage(*args, **kwargs)

    def __call__(self, test_args=None):
        """ Ensures that the "run()" method is called
        with the proper args and kwargs passed in from
        the optparser.

        test_args should only be used by testing, since
        it overrides optparse's automatic sys.argv parsing.
        """
        if test_args:
            options, args = self.parser.parse_args(test_args)
        else:
            options, args = self.parser.parse_args()
        options = dict(vars(options))
        args = list(args)
        try:
            self.run(*args, **options)
        except TypeError:
            # Are we hiding potential bugs with this?
            self.parser.print_usage()
            raise
            #sys.exit()

    def run(self, *args, **kwargs):
        """ This should be overwritten in the subclasses
        and actually "run" the appropriate process.
        """
        pass
