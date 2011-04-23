from tornado.web import Application as TornadoApp
from util import setLoggerLevel
import logging

class Application(TornadoApp):
    """ Simply reserving the right to override aspects
    of the base Application class at another point, and
    set the basic logger level until we find a better
    way.
    """

    def __init__(self, *args, **kwargs):
        # set logger level if provided
        loglevel = kwargs.get('loglevel')
        if loglevel and loglevel != "none":
            base_logger = logging.getLogger()
            setLoggerLevel(base_logger, loglevel)
        super(type(self), self).__init__(*args, **kwargs)
