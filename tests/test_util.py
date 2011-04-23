#!/usr/bin/env python

from unittest import TestCase
from torn.util import setLoggerLevel
import logging

class TestSetLoggerLevel(TestCase):

    def setUp(self):
        self.logger = logging.getLogger()

    def test_setLoggerLevel_bad(self):
        "non-existent levels should raise ValueError"
        self.assertRaises(ValueError, setLoggerLevel, self.logger, "bad")

    def test_setLoggerLevel_int(self):
        "an integer level should set the logger level"
        level = setLoggerLevel(self.logger, 10)
        self.assertEqual(level, 10)
        self.assertEqual(level, self.logger.level)

    def test_setLoggerLevel_debug(self):
        "a valid level should set the logger level"
        level = setLoggerLevel(self.logger, "debug")
        self.assertEqual(level, logging.DEBUG)
        self.assertEqual(level, self.logger.level)
