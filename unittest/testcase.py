import unittest
from main.githInteract import GithInteract, GitInteract


class TestCase(unittest.TestCase):
    def test_case(self):
        tt = GithInteract('')

        for each in tt.search_git_urls('', 0):
            g = GitInteract(each)
            g.git_clone_repo()


if __name__ == '__main__':
    unittest.main()
