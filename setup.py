#!/usr/bin/env python
"""
The MIT License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from distutils.core import setup

setup(
    name="torn",
    version="0.1",
    description="Tornado Utilities and Basic Framework",
    author="Jeremy Kelley and Josh Marshall",
    author_email="catchjosh@gmail.com",
    url = "http://github.com/joshmarshall/torn/",
    license = "http://www.opensource.org/licenses/mit-license.php",
    packages=["torn", "torn.manage"],
    package_data={"torn.manage": ["structure/*.py",
                                  "structure/static/css/*.css",
                                  "structure/static/js/*.js",
                                  "structure/templates/*.htm",
                                  "structure/app/*.py",
                                  "structure/app/views/*.py",
                                  "structure/app/views/uimodules/*.py"]},
    scripts=["scripts/torn-admin.py",],
    install_requires=["tornado",]
)
