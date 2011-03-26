from unittest import TestCase
from torn.manage.create import Create, ProjectAlreadyExists
import torn.manage
import os
import shutil
import tempfile
import sys

class TestCreate(TestCase):

    def setUp(self):
        self.tmp = self._create()

    def _create(self, **kwargs):
        tmp = tempfile.mkdtemp(prefix="torn_tmp_")
        os.rmdir(tmp)
        self.create = Create()
        self.create(tmp, **kwargs)
        return tmp

    def test_create(self):
        """ Test that all the proper files were created. """
        manage_dir = os.path.dirname(torn.manage.__file__)
        struct_dir = os.path.join(manage_dir, 'structure')
        files_to_test = []
        dirs_to_test = []
        for base, dirs, files in os.walk(struct_dir):
            for d in dirs:
                new_dir = os.path.join(base, d).replace(struct_dir, self.tmp)
                dirs_to_test.append(new_dir)
            for f in files:
                new_file = os.path.join(base, f).replace(struct_dir, self.tmp)
                files_to_test.append(new_file)
        for d in dirs_to_test:
            print d
            self.assertTrue(os.path.exists(d))
            self.assertTrue(os.path.isdir(d))
        for f in files_to_test:
            if f.endswith('.pyc'):
                self.assertFalse(os.path.exists(f))
            else:
                self.assertTrue(os.path.exists(f))
                self.assertTrue(os.path.isfile(f))

    def test_exists(self):
        """ Test that it won't try to recreate directory """
        self.assertRaises(ProjectAlreadyExists, self.create, self.tmp)

    def test_cookie_secret(self):
        """ Test that initial random cookie is generated for settings.py """
        test_secret = "this_is_my_secret"
        tmp = self._create(cookie_secret=test_secret)
        sys.path.append(tmp)
        from app.settings import settings
        self.assertEqual(settings['cookie_secret'], test_secret)
        shutil.rmtree(tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)
