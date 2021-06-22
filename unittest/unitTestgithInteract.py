#unitTestgithInteract.py
"""
    Unit Testing Suite for githInteract.py module
"""

import unittest
from main.githInteract import githInteract as g


class unitTestgithInteract(unittest.TestCase):
    token = 'Test token here'

    # def test_constructor(self):
    #    self.assertEqual(g(['poop'], '-a'), "Wrong username or password/input error:  list index out of range")

    def test_get_all_reponame(self):
        h = g(self.token, '-t')
        self.assertEqual(h.get_all_reponame(), ["tuple of repositories by full name"])
        #  print(h.get_all_reponame())

    def test_get_user(self):
        h = g(self.token, '-t')
        self.assertTrue(h.get_user())
        #  print(h.get_user())

    def test_get_userid(self):
        h = g(self.token, '-t')
        #  print(h.get_user_id())

    def test_get_repo_contents(self):
        h = g(self.token, '-t')
        h.get_repo_contents("Repository name here")

    def test_clone_repo(self):
        h = g(self.token, '-t')
        h.clone_repo("Repository name here")  # Tests write_change function
		
	def test_git_clone_repo(self):
        h = g1("Repository link here")
        h.git_clone_repo()


if __name__ == '__main__':
    unittest.main()
