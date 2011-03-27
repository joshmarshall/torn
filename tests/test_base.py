from unittest import TestCase
from torn.base import script, style

class TestDecorators(TestCase):

    def test_style(self):
        """ Verify that the css files are being added via decorator."""
        class Foo(object):
            @style("style.css")
            def get(self):
                pass
        foo = Foo()
        foo.get()
        self.assertTrue(hasattr(foo, '_css_files'))
        self.assertTrue(foo._css_files == ['style.css',])

    def test_script(self):
        """ Verify that the js files are being added via decorator."""
        class Foo(object):
            @script("jquery.js")
            def get(self):
                pass
        foo = Foo()
        foo.get()
        self.assertTrue(hasattr(foo, '_js_files'))
        self.assertTrue(foo._js_files == ['jquery.js',])
