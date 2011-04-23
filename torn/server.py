import tornado.httpserver
import tornado.ioloop
import logging

class Server(tornado.httpserver.HTTPServer):
    """ Reserving the right to override if necessary. """
    def serve(self, port, address=None):
        """ Simple IOLoop wrapper """
        if not address:
            address = ""
        self.listen(port, address=address)
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            logging.info("rcvd KeyboardInterrupt, exiting...")
