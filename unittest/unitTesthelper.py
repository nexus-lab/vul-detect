# unitTesthelper.py
"""
    Comprehensive test of the helper class
"""
from main.helper import Helper


def test_comprehensive():
    h = Helper('token here')
    urls = h.return_query_list('react', 5)  # Tests return_query_list
    repos, users = h.process_urls(urls)  # Tests run_scans and process_urls
    print(repos, users)

    # Comprehensive test of helper class
    user_graph = h.gen_user_graph(users)
    h.gen_user_graph(users, show=False, write=True)
    repo_graph = h.gen_repo_graph(repos)
    h.gen_repo_graph(repos, show=False, write=True)
    h.gen_bipartite_graph(users, repos)
    h.gen_bipartite_graph(users, repos, show=False, write=True)
    h.gen_clusterings(user_graph)
    h.gen_clusterings(repo_graph)  # Works only for more than one repo at a time
    h.gen_clusterings(user_graph, show=False, write=True)
    h.gen_clusterings(repo_graph, show=False, write=True)


if __name__ == '__main__':
    test_comprehensive()
