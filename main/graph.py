# graph.py
"""
    Module containing methods that construct graph representations using networkx library
"""
from process import vulnerabilityAssignment as v
import networkx
import networkx.drawing as nx
import matplotlib.pyplot as plt


class Graph:
    # TODO: Implement methods constructing graphs from scan data

    def __init__(self):
        pass

    def bipartite_construct(self, users, repos):
        # Input: List containing user objects and repo objects
        bipartite_graph = networkx.Graph()

        for user in users:
            bipartite_graph.add_nodes_from(user.get_users(), bipartite='users')
        for repo in repos:
            bipartite_graph.add_node(repo.get_name(), bipartite='repos')
        for repo in repos:
            for user in users:
                if user.repo == repo.get_name():
                    for name in user.names:
                        bipartite_graph.add_edge(name, repo.get_name())

        return bipartite_graph

    def graph_user(self, users):
        # Input: List of users objects
        # Output: user graph networkx object
        user_graph = networkx.Graph()
        all_vulns = {}

        for user in users:
            user_graph.add_nodes_from(user.get_users())
            all_vulns.update(user.get_vulns())

        for key, value in all_vulns.items():
            for key1, value1 in all_vulns.items():
                if key == key1:
                    pass
                else:
                    for item in value:
                        print('For user', key, ':', item, ' is equal to ', item, ' for user', key1)
                        if item in value1:
                            if user_graph.has_edge(key, key1):
                                pass
                            else:
                                user_graph.add_edge(key, key1)

        return user_graph

    def graph_repository(self, repos):
        # Input: list of repo objects
        # Output: repo graph networkx object
        repo_graph = networkx.Graph()
        all_vulns = {}

        for repo in repos:
            repo_graph.add_node(repo.get_name())
            all_vulns.update(repo.get_vulns())

        for key, value in all_vulns.items():
            for key1, value1 in all_vulns.items():
                if key == key1:
                    pass
                else:
                    for item in value:
                        print('For repo', key, ':', item, ' is equal to ', item, ' for repo', key1)
                        if item in value1:
                            if repo_graph.has_edge(key, key1):
                                pass
                            else:
                                repo_graph.add_edge(key, key1)

        return repo_graph

    def get_color_map(self, bipartite_graph):

        color_map = []
        repos = {n for n, d in bipartite_graph.nodes(data=True) if d["bipartite"] == 'repos'}

        for node in bipartite_graph:
            if node in repos:
                color_map.append('red')
            else:
                color_map.append('blue')

        return color_map
