#Testing.py
"""
Testing many features at once from different classes
"""

from main.githInteract import GitInteract, GithInteract
from main.scanner import Scanner as Sc
import networkx
import matplotlib.pyplot as plt
import networkx.drawing as nx
from process.users import Users
from process.repo import Repo
from main.graph import Graph
import process.vulnerabilityAssignment as va


token = ['']

# Instantiates GithInteract object with token above
g = GithInteract(token)
Graph = Graph()

# Instantiating objects for users, repos, and bipartite user-repo graphs
user_graph = networkx.Graph()
repo_graph = networkx.Graph()
bipartite_graph = networkx.Graph()

# Lists to store User and Repo objects
Repo_list = []
User_list = []

# Counter mainly used to help print information of each User object during for loop
User_counter = 0
Search_number = 5

# Returns a list of git urls with Python as query
repo_url_list = g.search_git_urls('network', Search_number)


for repo in repo_url_list:
    # Creates GitInteract object using git url and clones the repo onto system
    git = GitInteract(repo)
    temp_path = git.git_clone_repo()

    # Scan testing
    scans = Sc(temp_path)
    scans.bandit_scan()
    scans.flawfinder_scan()
    # scans.trufflehog_scan(git.url)
    scans.gitleaks_scan()

    # Appends Repo_list with a Repo object
    Repo_list.append(va.construct_repository(git.get_repo()))

    # Appends User_list with a User object
    User_list.append(va.construct_users(repo))

    # Prints out information from the User objects
    User_list[User_counter].print_info()
    User_counter += 1

# Adds nodes to user_graph based on the User_list

nx.draw(Graph.graph_user(User_list), with_labels=True)
plt.show()

# Adds nodes to repo_graph based on the Repo_list
nx.draw(Graph.graph_repository(Repo_list), with_labels=True)
plt.show()

bipartite_graph = Graph.bipartite_construct(User_list, Repo_list)
color_map = Graph.get_color_map(bipartite_graph)
nx.draw(bipartite_graph, node_color=color_map, with_labels=False)
plt.show()


