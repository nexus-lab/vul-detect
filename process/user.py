# user.py

#TODO: Add vulnerability setter method
class User():

    def __init__(self, names, repo):
        # list, string
        self.names = names
        self.repo = repo

    def get_users(self):
        # Returns list of names
        return self.names

    def print_info(self):
        # Prints the users and repo name associated with them
        return print(f'Repository: {self.repo}\nUsers: {self.names}\n')