# repo.py
"""
    Module containing class representing repositories
"""


class Repo:

    def __init__(self, name, vulns):
        """
        Repo object constructor

        :param name: name of repo, string
        :param vulns: dictionary of vulnerabilities
        """
        self.name = name
        self.vulns = vulns

    def get_name(self):
        """
        Returns name

        :return: name of repo, string
        """
        return self.name

    def get_vulns(self):
        """
        Returns vulnerabilities

        :return: dictionary of vulnerabilities
        """
        return self.vulns
