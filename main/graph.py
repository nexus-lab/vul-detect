# graph.py
"""
    Module containing methods that construct graph representations using networkx library
"""
import networkx
import matplotlib.pyplot as plt
from karateclub import DeepWalk
from sklearn.decomposition import PCA


class Graph:

    def __init__(self):
        pass

    def bipartite_construct(self, users, repos):
        """
        Bipartite graph edges representing contributing users

        :param users: Users object containing list of users
        :param repos: Repo object containing list of repos
        :return: networkx bipartite graph object
        """
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
        """
        Monopartite graphical representation of users based on vulnerabilities

        :param users: List of users objects
        :return: networkx monopartite graph of users
        """
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
                        # print('For user', key, ':', item, ' is equal to ', item, ' for user', key1)
                        if item in value1:
                            if user_graph.has_edge(key, key1):
                                pass
                            else:
                                user_graph.add_edge(key, key1)

        return user_graph

    def graph_repository(self, repos):
        """
        Monopartite graphical representation of repos based on vulnerabilities

        :param repos: List of repo objects
        :return: networkx monopartite graph of repos
        """
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
                        # print('For repo', key, ':', item, ' is equal to ', item, ' for repo', key1)
                        if item in value1:
                            if repo_graph.has_edge(key, key1):
                                pass
                            else:
                                repo_graph.add_edge(key, key1)

        return repo_graph

    def get_color_map(self, bipartite_graph):
        """
        Constructs color map of bipartite graph

        :param bipartite_graph: networkx bipartite graph
        :return: List containing color mappings for graph
        """
        color_map = []
        repos = {n for n, d in bipartite_graph.nodes(data=True) if d["bipartite"] == 'repos'}

        for node in bipartite_graph:
            if node in repos:
                color_map.append('red')
            else:
                color_map.append('blue')

        return color_map

    def gen_embeddings(self, graph):
        """
        DeepWalk implementation

        :param graph: networkx graph
        :return: produced embeddings from input graph
        """
        model = DeepWalk(walk_length=100, dimensions=64, window_size=5)
        model.fit(graph)
        embeddings = model.get_embedding()
        return embeddings

    def show_cluster(self, node_no, embedding):
        """
        Outputs graphical representation of graph embeddings

        :param node_no: number of nodes to display
        :param embedding: matrix containing embeddings
        :return: graph
        """
        nodes = embedding[node_no]

        pca = PCA(n_components=2)
        pca_out = pca.fit_transform(nodes)

        plt.figure(figsize=(15, 10))
        plt.scatter(pca_out[:, 0], pca_out[:, 1])
        for i, node in enumerate(node_no):
            plt.annotate(node, (pca_out[i, 0], pca_out[i, 1]))

        plt.show()
