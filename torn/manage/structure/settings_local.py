""" Override any default settings here.
NOTE: You should always put a sane development default settings in
<BASE>/<APP>/settings.py first, and then set any deployment specific
settings here. While the <BASE>/<APP>/settings.py file SHOULD be under
version control, this file should NEVER be.

If you don't need to override any settings, you can delete this file.
"""

settings = dict(
    # deployment specific settings go here
    # for example, the default "address" setting is
    # set to "" by default under <BASE>/<APP>/settings.py,
    # and the port is set to 8080.
    # To override these settings in deployment, uncomment
    # the following lines:
    #
    # port = 8001,
    # address = "127.0.0.1" # makes direct access localhost-only
)
