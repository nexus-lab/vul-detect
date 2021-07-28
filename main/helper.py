# helper.py
"""
    Helper class - methods that perform important roles in producing graph visualizations of scan metrics
"""
from main.githInteract import GitInteract as git
from main.scanner import Scanner
from main.graph import Graph
from main import utility
import process.vulnerabilityAssignment as va
import multiprocessing as cpu
import os
import networkx
import matplotlib.pyplot as plt
import networkx.drawing as nx


class Helper:
    # TODO: Change write section of functions to include metadata

    def __init__(self, githInteract):
        """
        Constructor

        :param githInteract: Instatiated githInteract object
        :param gitInteract: Instantiated gitInteract object
        """
        self._gith = githInteract
        self.graph = Graph()

    def return_query_list(self, query, number):
        """
        Returns list of urls based on search query

        :param query: string of query, see GitHub api
        :param number: number of repos to search
        :return: list of urls
        """
        return self._gith.search_git_urls(query, number)

    def run_scans(self, path):
        # TODO: Optimize
        """
        Operates scans with use of multithreading

        :param path: path to repository
        """
        scanner = Scanner(path)

        try:
            s1 = cpu.Process(target=scanner.bandit_scan())
            s2 = cpu.Process(target=scanner.flawfinder_scan())
            s3 = cpu.Process(target=scanner.gitleaks_scan())

            s1.start()  # Start bandit scan
            s2.start()  # Start flawfinder scan
            s3.start()  # Start gitleaks scan

            s1.join()  # Wait for bandit scan
            s2.join()  # Wait for flawfinder scan
            s3.join()  # Wait for gitleaks scan
            print(f'Scans for {path} finished')
        except Exception:
            raise RuntimeError('Issue running scans for: ' + path)

    def process_urls(self, url_list):
        """
        Downloads repos and performs scans

        :param url_list: list of git urls
        :return: repo and user list
        """
        repo_list = list()
        user_list = list()
        user_counter = 0

        for repo in url_list:
            repog = git(repo)
            path = repog.git_clone_repo()

            self.run_scans(path)

            repo_list.append(va.construct_repository(repog.get_repo()))
            user_list.append(va.construct_users(repo))

            user_list[user_counter].print_info()
            user_counter += 1

        utility.clear_temp()  # Deletes temp folder
        return repo_list, user_list

    def gen_user_graph(self, user_list, show=True, write=False):
        """
        Creates user graph using list of users objects

        :param user_list: list of users objects
        :param show: boolean value indicating use of plotlib
        :param write: boolean value indicating to write to file or not
        :return: networkx graph
        """
        user_graph = self.graph.graph_user(user_list)

        if show:
            nx.draw(user_graph, with_labels=True)
            plt.show()
        if write:
            networkx.write_gexf(user_graph, os.getcwd() + '/users.gexf')

        return user_graph

    def gen_repo_graph(self, repo_list, show=True, write=False):
        """
        Creates repo graph using list of repo objects

        :param repo_list: list of repo objects
        :param show: boolean value indicating use of plotlib
        :param write: boolean value indicating to write to file or not
        :return: networkx graph
        """
        repo_graph = self.graph.graph_repository(repo_list)

        if show:
            nx.draw(repo_graph, with_labels=True)
            plt.show()
        if write:
            networkx.write_gexf(repo_graph, os.getcwd() + '/repos.gexf')

        return repo_graph

    def gen_bipartite_graph(self, user_list, repo_list, show=True, write=False):
        """
        Creates bipartite graph using list of users and repo objects

        :param user_list: list of users objects
        :param repo_list: list of repo objects
        :param show: boolean value indicating use of plotlib
        :param write: boolean value indicating to write to file or not
        :return: networkx graph
        """
        bipartite_graph = self.graph.bipartite_construct(user_list, repo_list)
        color_map = self.graph.get_color_map(bipartite_graph)

        if show:
            nx.draw(bipartite_graph, node_color=color_map, with_labels=False)
            plt.show()
        if write:
            networkx.write_gexf(bipartite_graph, os.getcwd() + '/usertorepo.gexf')

        return bipartite_graph

    def gen_clusterings(self, graph, show=True, write=False):
        # TODO: Needs way of altering figure dimensions for larger data sets
        # TODO: Needs way of displaying repo and user names
        """
        Graph clustering to show dimensional relationship between nodes

        :param graph: networkx graph
        :param show: boolean value indicating use of plotlib
        :param write: boolean value indicating whether to write to file or not
        :return: window or file
        """
        label_info = str()
        int_graph = networkx.convert_node_labels_to_integers(graph, label_attribute=label_info)
        embeddings = self.graph.gen_embeddings(int_graph)
        nodes = list(range(len(embeddings)))

        if show:
            self.graph.show_cluster(nodes, embeddings)
        if write:
            self.graph.show_cluster(nodes, embeddings, save_file=True)
