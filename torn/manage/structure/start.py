"""
This file will launch a single instance of the app. You
can overwrite settings, pass in db connections, etc. as directed
below.
"""

from torn.application import Application
from torn.server import Server
from torn.util import parse_command_line
from app.views import routes
from app.views import uimodules
from app.settings import settings
import logging

def main():
    parse_command_line(settings)

    # Add settings attributes here, i.e.:
    # settings.db = database_connect()

    settings.ui_modules = uimodules

    application = Application(routes, **settings)
    logging.info("Starting app at %s:%s" % (settings.address, settings.port))
    server = Server(application)
    server.serve(settings.port, address=settings.address)

if __name__ == "__main__":
    main()
