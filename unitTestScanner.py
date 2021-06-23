#UnitTestScanner.py
"""
    Unit Test Suite for Scanner Class
"""

import unittest
from main.scanner import Scanner as s
from main import utility

class UnitTestScanner(unittest.TestCase):
    path = utility.return_path() + '\\temp'

    def setUp(self):
        # Creates this scanner object before every test
        # Prevents from repeating code
        self.t = s(self.path)

    def test_bandit_scan(self):
        self.t.bandit_scan()

    def test_flawfinder_scan(self):
        self.t.flawfinder_scan()

if __name__ == '__main__':
    unittest.main()
