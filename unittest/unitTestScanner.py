# unitTestScanner.py
"""
    Unit Test Suite for Scanner Class
"""

import unittest
from main.scanner import Scanner as s
from main import utility


class UnitTestScanner(unittest.TestCase):
    path = utility.return_path() + '\\temp'
    token = ['']

    def setUp(self):
        # Creates this scanner object before every test
        # Prevents from repeating code
        self.t = s(self.path)

    def test_bandit_scan(self):
        self.t.bandit_scan()

    def test_flawfinder_scan(self):
        self.t.flawfinder_scan()

    def test_trufflehog_scan(self):
        # e = ['git://github.com/donnemartin/system-design-primer.git', 'git://github.com/public-apis/public-apis.git', 'git://github.com/TheAlgorithms/Python.git', 'git://github.com/jackfrued/Python-100-Days.git', 'git://github.com/vinta/awesome-python.git', 'git://github.com/ytdl-org/youtube-dl.git', 'git://github.com/tensorflow/models.git', 'git://github.com/nvbn/thefuck.git', 'git://github.com/django/django.git', 'git://github.com/pallets/flask.git']
        # for each in e:
        self.t.trufflehog_scan('')

    def test_gitleaks_scan(self):
        t = s(utility.return_path() + "")
        t.gitleaks_scan()


if __name__ == '__main__':
    unittest.main()
