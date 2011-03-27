"""
Various miscellaneous utilites for starting and managing
Tornado instances.
"""
from optparse import OptionParser
import sys

# Default command parser
PARSER = OptionParser()
PARSER.add_option("-r", "--routes", action="store_true",
                  help="print list of routes and exit")
PARSER.add_option("-p", "--port", type="int",
                  help="set http server port")
PARSER.add_option("-l", "--loglevel", default="info",
                  help="set the logging level",
                  metavar="info|warning|error|none")

def parse_command_line(settings):
    """ Parses the command line options """
    options, args = PARSER.parse_args()
    if options.routes:
        # not sure I like this import assumption...
        from views import routes
        L = max( len(r.reverse()) for r in views.routes ) # len of longest path
        fmt = "    %%-%ds => %%s" % L
        for r in routes:
            print fmt % (r.reverse(), ".".join((
                r.handler_class.__modules__,
                r.handler_class.__name__)))
        sys.exit(0)
    elif options.port:
        try:
            settings.port = int(options.port)
        except ValueError:
            pass
    if options.loglevel:
        settings.loglevel = options.loglevel
    return settings
