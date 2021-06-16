#unitTestScanner.py
"""
    Unit Test Suite for Scanner Class
    NOTE: It is recommended to run unitTestgithInteract.py pre-emptively 
"""

import unittest
from main.scanner import scanner as s
from main import utility

class unitTestScanner(unittest.TestCase):
    path = utility.return_path() + '/temp/'

    def test_bandit_scan(self):
        t = s(self.path)
        t.bandit_scan()

    def test_flawfinder_scan(self):
        t = s(self.path)  # s(utility.return_path())
        t.flawfinder_scan()

if __name__ == '__main__':
    unittest.main()
