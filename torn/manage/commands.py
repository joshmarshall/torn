""" A list of commands that torn.py supports """

from torn.manage.create import Create
from torn.manage.launch import Launch
import sys
from os.path import basename

COMMANDS = dict(create=Create,
                start=Launch)

class UnknownCommand(Exception):
    pass

def run_command(command_name):
    command_class = COMMANDS.get(command_name)
    if not command_class:
        raise UnknownCommand(command_name)
    command = command_class()
    command()

def usage():
    print "USAGE:"
    print "%s %s [OPTIONS...]" % (basename(sys.argv[0]),
                                  '|'.join(COMMANDS.keys()))
    sys.exit(1)

def run_command_line():
    if len(sys.argv) < 2:
        return usage()
    command = sys.argv.pop(1)
    try:
        run_command(command)
    except UnknownCommand:
        return usage()
