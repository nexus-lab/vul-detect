#UnitTestGithInteract.py
"""
    Unit Testing Suite for githInteract.py module
"""

import unittest
from main.githInteract import GithInteract as g


class UnitTestGithInteract(unittest.TestCase):
    token = ['insert account token here']


    # def test_constructor(self):
    #    self.assertEqual(g(['poop'], '-a'), "Wrong username or password/input error:  list index out of range")

    def test_get_all_reponame(self):
        h = g(self.token)
        self.assertEqual(h.get_all_reponame(), ["nexus-lab/vul-detect"])
        # print(h.get_all_reponame())

    def test_get_user(self):
        h = g(self.token)
        self.assertTrue(h.get_user())
        #  print(h.get_user())

    def test_get_userid(self):
        h = g(self.token)
        #  print(h.get_user_id())

    def test_get_repo_contents(self):
        h = g(self.token)
        h.get_repo_contents("nexus-lab/vul-detect")

    def test_clone_repo(self):
        h = g(self.token)
        h.clone_repo("nexus-lab/vul-detect")  # Tests write_change function


if __name__ == '__main__':
    unittest.main()
