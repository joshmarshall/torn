"""
Provides a clean method for importing default settings and
user override settings.
"""

from tornado.web import _O

def load_settings(user_settings):
    """ Parse user settings, imports local settings, etc. """
    try:
        import settings_local
        user_settings.update(settings_local.settings)
    except ImportError:
        pass

    settings = _O(user_settings)
    return settings
