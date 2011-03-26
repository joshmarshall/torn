"""
This file contains all of the default settings for your app.
You should add anything "default" parameters (i.e. dummy api keys,
local database connection information, etc.) in this file, but
for deployment specific options, you should create a settings_local.py
file and overwrite the changes.
"""

from torn.config import load_settings
from os.path import join, dirname, abspath

settings = load_settings(dict(

    # Add your settings here
    port = 8080,
    address = "",
    debug = True,
    cookie_secret = "<COOKIE_SECRET>",
    xsrf_cookies = True,
    static_path = abspath(join(dirname(__file__), "../static")),
    template_path = abspath(join(dirname(__file__), "../templates")),

))
