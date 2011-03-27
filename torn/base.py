import functools
from tornado.web import RequestHandler, authenticated, asynchronous

class Handler(RequestHandler):

    def render_string(self, template, **kwargs):
        css_files = []
        js_files = []
        if hasattr(self, '_css_files'):
            css_files = self._css_files
        kwargs.setdefault('css_files', css_files)
        if hasattr(self, '_js_files'):
            js_files = self._js_files
        kwargs.setdefault('js_files', js_files)
        return super(Handler, self).render_string(template, **kwargs)


def style(*styles):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            if not hasattr(self, '_css_files'):
                self._css_files = []
            for style in styles:
                self._css_files.append(style)
            return f(self, *args, **kwargs)
        return wrapped
    return wrapper


def script(*scripts):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            if not hasattr(self, '_js_files'):
                self._js_files = []
            for script in scripts:
                self._js_files.append(script)
            return f(self, *args, **kwargs)
        return wrapped
    return wrapper
