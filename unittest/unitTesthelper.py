# unitTesthelper.py
"""
    Comprehensive test of the helper class
"""
import unittest
from main.helper import Helper
from main.githInteract import GithInteract


class UnitTesthelper(unittest.TestCase):
    g = GithInteract('token here')
    h = Helper(g)
    urls = h.return_query_list('language:python', 5)  # Tests return_query_list
    repos, users = h.process_urls(urls)  # Tests run_scans

    def test_gen_user_graphs(self):
        self.h.gen_user_graph(self.users)
        self.h.gen_user_graph(self.users, show=False, write=True)

    def test_gen_repo_graphs(self):
        self.h.gen_repo_graph(self.repos)
        self.h.gen_repo_graph(self.repos, show=False, write=True)

    def test_gen_bipartite_graphs(self):
        self.h.gen_bipartite_graph(self.users, self.repos)
        self.h.gen_bipartite_graph(self.users, self.repos, show=False, write=True)

    def test_gen_clusterings(self):
        self.h.gen_clusterings(self.users)
        self.h.gen_clusterings(self.repos)
        self.h.gen_clusterings(self.users, show=False, write=True)
        self.h.gen_clusterings(self.repos, show=False, write=True)


if __name__ == '__main__':
    unittest.main()
