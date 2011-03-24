import sys
import os

class Launch(object):

    name = "start"

    def __call__(self, directory, *args, **kwargs):
        sys.path.append(os.path.abspath(directory))
        import start
        start.main()
