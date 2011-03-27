"""
This is just a sample handler to get you started. Read
the tornado documentation at http://www.tornadoweb.org
to get started using request handlers.
"""

from torn.base import Handler, style, script
from torn.route import route

@route("/", name="index")
class IndexHandler(Handler):

    @script("jquery.js", "index.js")
    @style("style.css")
    def get(self):
        """ Simply renders the index template. """
        return self.render("index.htm")
