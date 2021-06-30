# githInteract.py
"""
    Module containing methods with ability to interact with Github API v3
    PyGithub required dependency
    pygit2 required dependency
"""

from github import Github  # GitHub interaction, exception handling
from main import utility as u  # Utility methods
import pygit2   # Git command interaction
import os   # OS interaction
import shutil  # Directory management


class GithInteract:
    # TODO: Add exception handling for hourly call limit

    def __init__(self, inpt):
        # Must provide tuple/list[username, password] or str(token)
        if len(inpt) == 1 or type(inpt) == str:
            if type(inpt) == str:
                self._g = Github(inpt)
            else:
                self._g = Github(inpt[0])
            self.ratelimit = self._g.get_rate_limit()
        elif len(inpt) == 2:
            self._g = Github(inpt[0], inpt[1])
            self.ratelimit = self._g.get_rate_limit()
        else:
            raise ValueError("Improper input length. Input must be list of one to two strings")

    def get_all_reponame(self):
        # Returns a list of repos associated with GitHub account
        names = list()

        for repo in self._g.get_user().get_repos():
            names.append(repo.full_name)

        return names

    def get_user(self):
        # Return user name of associated GitHub account
        return self._g.get_user().name

    def get_user_id(self):
        # Return user id of associated GitHub account
        return self._g.get_user().id

    def get_git_url_repo(self, rName):
        # Return git url of repo associated with GitHub account
        return self._g.get_repo(rName).git_url

    def get_repo_contents(self, rName):
        # TODO: Exception handling for invalid name
        # Return list contents of given repo
        repo = self._g.get_repo(rName)
        internal = repo.get_contents("")
        contents = list()

        while internal:
            files = internal.pop(0)
            if files.type == "dir":
                internal.extend(repo.get_contents(files.path))
            else:
                contents.append(files)

        return contents

    def get_collaborators(self, rName):
        # Returns list of collaborators associated with repo
        r = self._g.get_repo(rName)
        collab_names = []

        for each in r.get_collaborators():
            collab_names.append(each.name)

        return collab_names

    def search_git_urls(self, query, count):
        # Returns list of git urls based on query
        repo = self._g.search_repositories(query=query)
        repolist = []
        i = 0

        for repos in repo:
            repolist.append(repos.git_url)
            i += 1
            if i == count:
                break

        return repolist

    def clone_repo(self, rName):
        # Clones input repo name for associated account
        # Returns path to cloned repo
        # TODO: Add identifier tied to cloned repository
        repo = self._g.get_repo(rName)
        path = os.getcwd() + '/temp/' + rName

        try:
            pygit2.clone_repository(repo.git_url, path)
        except ValueError:
            shutil.rmtree(path, onerror=u.write_change)
            shutil.rmtree(path, ignore_errors=True)  # Kind of crude, but it works
            pygit2.clone_repository(repo.git_url, path)

        return path


class GitInteract:
    # Object associated with provided git url
    # TODO: Cleanup code, consider separate module

    def __init__(self, url):
        # Constructor - instantiates working path based on given url
        self.url = url
        self.path = u.return_path() + '\\temp'
        for each in url.split('/'):  # To return the object associated with the git object
            if each == 'github.com' or each == '' or each == 'https:' or each == 'git:':
                pass
            else:
                self.path = self.path + '/' + each.split('.')[0]  # Apparently '\\' doesn't work???
        self.org = self.path.split('/')[-2]
        self.repo = self.path.split('/')[-1]

    def git_clone_repo(self):
        # Clones repo based on input git link

        try:
            pygit2.clone_repository(self.url, self.path)
        except ValueError:
            shutil.rmtree(self.path, onerror=u.write_change)
            shutil.rmtree(self.path, ignore_errors=True)  # Kind of crude, but it works
            pygit2.clone_repository(self.url, self.path)

        return self.path

    def git_collaborators(self):
        # Needs path to .git
        repo = pygit2.Repository(self.path)
        names = []

        for commit in repo.walk(repo.head.target):
            if commit.author.name in names:
                pass
            else:
                names.append(commit.author.name)

        sorted_names = sorted(names)

        return sorted_names

    def get_organization(self):
        # Return organization name
        return self.org

    def get_repo(self):
        # Return repository name
        return self.repo
