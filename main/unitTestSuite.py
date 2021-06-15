#unitTestSuite.py
"""
    Unit Testing Suite for githInteract.py module
    NOTE: Unfilled version of unitTestSuite module
"""

import unittest 
from githInteract import githInteract as g

class unitTestSuite(unittest.TestCase):
    token = 'Test Token Here'
    #TODO: Needs test of constructor using username and password

    def test_get_all_reponame(self):
        h = g(self.token, '-t')
        self.assertEqual(h.get_all_reponame(), ["list of repositories by full name"])
        print(h.get_all_reponame())

    def test_get_user(self):
        h = g(self.token, '-t')
        self.assertTrue(h.get_user())
        print(h.get_user())

    def test_get_userid(self):
        h = g(self.token, '-t')
        print(h.get_user_id())

    def test_get_repo_contents(self):
        h = g(self.token, '-t')
        h.get_repo_contents("Repository name here")

    def test_clone_repo(self):
        h = g(self.token, '-t')
        h.clone_repo("Repository name here")  # Tests write_change function


if __name__ == '__main__':
    unittest.main()