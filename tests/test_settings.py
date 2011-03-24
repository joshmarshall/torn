from unittest import TestCase
from torn.config import load_settings

class TestSettings(TestCase):

    def test_load(self):
        settings = {"port": 8000}
        settings = load_settings(settings)
        self.assertTrue(settings.port == 8000)
