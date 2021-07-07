# users.py
"""
    Module containing class representing users of a repo.
"""
# TODO: Add vulnerability setter method


class Users:

    def __init__(self, names, repo, vulns):
        # list, string
        self.names = names
        self.repo = repo
        self.vulns = vulns

    def get_users(self):
        # Returns list of names
        return self.names

    def print_info(self):
        # Prints the users and repo name associated with them
        return print(f'Repository: {self.repo}\nUsers: {self.names}\n')

    def get_vulns(self):
        return self.vulns