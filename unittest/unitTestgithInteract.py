#UnitTestGithInteract.py
"""
    Unit Testing Suite for githInteract.py module
"""

import unittest
from main.githInteract import GithInteract as g
from main.githInteract import GitInteract as g1


class UnitTestGithInteract(unittest.TestCase):
    token = ['Test token here']


    # def test_constructor(self):
    #    self.assertEqual(g(['poop'], '-a'), "Wrong username or password/input error:  list index out of range")

    def setUp(self):
        self.h = g(self.token)

    def test_get_all_reponame(self):
        self.assertEqual(self.h.get_all_reponame(), ["List of repositories by full name"])
        # print(h.get_all_reponame())

    def test_get_user(self):
        self.assertTrue(self.h.get_user())
        #  print(h.get_user())

    def test_get_userid(self):
        self.assertTrue(self.h.get_user_id())
        #  print(h.get_user_id())

    def test_get_repo_contents(self):
        self.h.get_repo_contents("Repository name here")

    def test_clone_repo(self):
        self.h.clone_repo("Repository name here")  # Tests write_change function

    def test_git_clone_repo(self):
        h = g1("Repository link here")
        h.git_clone_repo()

if __name__ == '__main__':
    unittest.main()
