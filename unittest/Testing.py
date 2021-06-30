#Testing.py
"""
Testing many features at once from different classes
"""

from main.githInteract import GitInteract, GithInteract
from main.scanner import Scanner
import networkx
import matplotlib.pyplot as plt
import networkx.drawing as nx
from process.user import User
from process.repo import Repo

token = ['']

# Instantiates GithInteract object with token above
g = GithInteract(token)

# Instantiating objects for users, repos, and bipartite user-repo graphs
user_graph = networkx.Graph()
repo_graph = networkx.Graph()
bipartite_graph = networkx.Graph()

# Lists to store User and Repo objects
Repo_list = []
User_list = []

# Counter mainly used to help print information of each User object during for loop
User_counter = 0

# Returns a list of git urls with Python as query
repo_url_list = g.search_git_urls('language:Python', 5)


for repo in repo_url_list:
    # Creates GitInteract object using git url and clones the repo onto system
    git = GitInteract(repo)
    git.git_clone_repo()

    # Appends Repo_list with a Repo object
    Repo_list.append(Repo(git.get_repo()))

    # Appends User_list with a User object
    User_list.append(User(git.git_collaborators(), git.get_repo()))

    # Prints out information from the User objects
    User_list[User_counter].print_info()
    User_counter += 1

# Adds nodes to user_graph based on the User_list
for index in range(5):
    user_graph.add_nodes_from(User_list[index].get_users())

# Displays user_graph
nx.draw(user_graph, with_labels=True)
plt.show()

# Adds nodes to repo_graph based on the Repo_list
for index in range(5):
    repo_graph.add_node(Repo_list[index].get_name())

# Displays repo_graph
nx.draw(repo_graph, with_labels=True)
plt.show()

# Adds two sets of nodes to bipartite_graph: one for users and one for repos
for index in range(5):
    bipartite_graph.add_nodes_from(User_list[index].get_users(), bipartite='users')

for index in range(5):
    bipartite_graph.add_node(Repo_list[index].get_name(), bipartite='users')

# Nested for loop in order to create edges between users and their repos
for index in range(5):
    for user in User_list[index].get_users():
        bipartite_graph.add_edge(user, Repo_list[index].get_name())

# Displays bipartite_graph
nx.draw(bipartite_graph, with_labels=True)
plt.show()