# users.py
"""
    Module containing class representing users of a repo.
"""


class Users:

    def __init__(self, names, repo, vulns):
        """
        Users object constructor

        :param names: list containing names of users
        :param repo: repo associated with users, string
        :param vulns: dictionary of vulnerabilities
        """
        self.names = names
        self.repo = repo
        self.vulns = vulns

    def get_users(self):
        """
        Returns list of names

        :return: list of users names
        """
        return self.names

    def print_info(self):
        """
        Prints the users and repo name associated with them

        :return: print statement (consider changing)
        """
        return print(f'Repository: {self.repo}\nUsers: {self.names}\n')

    def get_vulns(self):
        """
        Returns dictionary of vulnerabilities

        :return: dictionary of vulnerabilities associated with users
        """
        return self.vulns
