# repo.py
"""
    Module containing class representing repositories
"""
# TODO: Add vulnerability setter method


class Repo:

    def __init__(self, name, vulns):
        # String, dictionary
        self.name = name
        self.vulns = vulns

    def get_name(self):
        # Returns name
        return self.name

    def get_vulns(self):
        # Returns vulnerabilities
        return self.vulns