from tornado.web import _O

def load_settings(user_settings):
    """ Parse user settings, imports local settings, etc. """
    try:
        from settings import settings as local_settings
        user_settings.update(local_settings)
    except ImportError:
        pass

    settings = _O(user_settings)
    return settings
