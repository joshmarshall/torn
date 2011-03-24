from tornado.web import Application as TornadoApp
import logging

class Application(TornadoApp):
    """ Simply reserving the right to override aspects
    of the base Application class at another point, and
    set the basic logger level until we find a better
    way.
    """
    
    def __init__(self, *args, **kwargs):
        # There HAS to be a better way to do this...
        loglevel = kwargs.get('loglevel')
        if loglevel and loglevel != "none":
            base_logger = logging.getLogger()
            if loglevel == "debug":
                base_logger.setLevel(logging.DEBUG)
            elif loglevel == "info":
                base_logger.setLevel(logging.INFO)
            elif loglevel == "warning":
                base_logger.setLevel(logging.WARNING)
            elif loglevel == "error":
                base_logger.setLevel(logging.ERROR)
        super(type(self), self).__init__(*args, **kwargs)

