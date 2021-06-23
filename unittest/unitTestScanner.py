#unitTestScanner.py
"""
    Unit Test Suite for Scanner Class
"""

import unittest
from main.scanner import scanner as s
from main import utility

class unitTestScanner(unittest.TestCase):
    path = utility.return_path() + '\\temp'
	token = 'Add token here'

    def test_bandit_scan(self):
        t = s(self.path)
        t.bandit_scan()

    def test_flawfinder_scan(self):
        t = s(self.path)  # s(utility.return_path())
        t.flawfinder_scan()
		
	def test_trufflehog_scan(self):
		t = s(self.path)
		t.trufflehog_scan("https://github.com/trufflesecurity/truffleHog.git")

    def test_gitleaks_scan(self):
        t = s(utility.return_path() + "/temp/nexus-lab/vul-detect")
        t.gitleaks_scan()

if __name__ == '__main__':
    unittest.main()
