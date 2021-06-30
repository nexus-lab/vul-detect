# repo.py
from org import Org


class Repo(Org):

    def __init__(self, name, vulns):
        # String, dic
        self.name = name
        self.vulns = vulns

