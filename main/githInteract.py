# githInteract.py
'''
    Module containing methods with ability to interact with Github API v3
    PyGithub required dependency
'''

from github import Github

class githInteract:
    # TODO: Add exception handling for hourly call limit

    def __init__(self, token):
        # Object requires token
        self._g = Github(token)


    def get_all_reponame(self):
        # Returns a list of names in repo of instantiated object
        names = list()

        for repo in self._g.get_user().get_repos():
            names.append(repo.name)

        return names

    def get_user(self):
        # Return user name of assigned github repo
        r = self._g.get_user().name
        return r

    def get_repo_contents(self, rName):
        # TODO: Exception handling for invalid name
        # Get content of given repo
        repo = self._g.get_repo(rName)
        internal = repo.get_contents("")

        while internal:
            # TODO: Adapt to hard coded data rather than directory listing
            files = internal.pop(0)
            if files.type == "dir":
                internal.extend(repo.get_contents(files.path))
            else:
                print(files)
