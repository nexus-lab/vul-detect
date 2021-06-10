#unitTestSuite.py
'''
    Unit Testing Suite for githInteract.py module
    NOTE: Modified blank
'''

import unittest

from githInteract import githInteract as g

class unitTestSuite(unittest.TestCase):
    token = '# Add token here'

    def test_get_all_reponame(self):
        h = g(self.token)
        self.assertEqual(h.get_all_reponame(), ['# Add test case list here'])
        print(h.get_all_reponame())

    def test_get_user(self):
        h = g(self.token)
        self.assertTrue(h.get_user())
        print(h.get_user())

    def test_get_repo_contents(self):
        h = g(self.token)
        h.get_repo_contents("# Add repository name here")

if __name__ == '__main__':
    unittest.main()