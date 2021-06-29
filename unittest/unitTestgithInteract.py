# unitTestGithInteract.py
"""
    Unit Testing Suite for githInteract.py module
"""

import unittest
from main.githInteract import GithInteract as g
from main.githInteract import GitInteract as g1


class UnitTestGithInteract(unittest.TestCase):
    token = ['']
    # TODO: Needs update to test all methods

    def setUp(self):
        self.h = g(self.token)

    def test_get_all_reponame(self):
        self.assertEqual(self.h.get_all_reponame(), [""])

    def test_get_user(self):
        self.assertTrue(self.h.get_user())

    def test_get_userid(self):
        self.assertTrue(self.h.get_user_id())

    def test_get_repo_contents(self):
        self.h.get_repo_contents("")

    def test_clone_repo(self):
        self.h.clone_repo("")  # Tests write_change function

    def test_search_git_urls(self):
        print(self.h.search_git_urls('', 0))

    def test_git_clone_repo(self):
        h = g1("")
        h.git_clone_repo()

    def test_get_collaborators(self):
        self.assertEqual(self.h.get_collaborators(''), [''])

    def test_git_collaborators(self):
        e3 = g1('')
        print(e3.git_collaborators())


if __name__ == '__main__':
    unittest.main()
