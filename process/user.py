# user.py
from org import Org


class User(Org):

    def __init__(self, name, repos, vulns):
        # Str, list, dic
        self.name = name
        self.repos = repos
        self.vuln = vulns
