from unittest import TestCase
from torn.manage.create import Create, ProjectAlreadyExists
import torn.manage
import torn.config
import os
import sys
import shutil
import tempfile

class TestCreate(TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="torn_tmp_")
        os.rmdir(self.tmp)
        self.create = Create()
        self.create(self.tmp)

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

    def test_settings(self):
        """ Test that settings parameters are properly set
        and also properly overidden.
        """
        test_settings = torn.config.load_settings({"port": 8000})
        self.assertTrue(test_settings.port == 8000)
        port = 1337
        content = """settings={"port":%d}""" % port
        path = os.path.join(self.tmp, "settings_local.py")
        fp = open(path, "w")
        fp.write(content)
        fp.close()
        sys.path.append(self.tmp)
        import app.settings
        sys.path.remove(self.tmp)
        self.assertTrue(app.settings.settings.port == port)

    def tearDown(self):
        shutil.rmtree(self.tmp)
