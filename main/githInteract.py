# githInteract.py
"""
    Module containing methods with ability to interact with Github API v3
    PyGithub required dependency
    pygit2 required dependency
"""

from github import Github, GithubException  # GitHub interaction, exception handling
from main import utility as u  # Utility methods
import pygit2   # Git command interaction
import os   # OS interaction
import shutil  # Directory management
from main.vulErrors import TokenError, PasswordUserError  # Class exception handling


class githInteract:
    # TODO: Add exception handling for hourly call limit

    def __init__(self, inpt, *args):
        # Args = -a Tuple = [Username, Password], -t Str = Token
        if '-t' in args:
            try:
                self._g = Github(inpt)
            except (GithubException, TypeError, ValueError, IndexError) as e:
                raise TokenError(e)
        elif '-a' in args:
            try:
                self._g = Github(inpt[0], inpt[1])
            except (GithubException, TypeError, ValueError, IndexError) as e:
                raise PasswordUserError(e)
        else:
            raise ValueError("Improper argument, must declare -a or -t.")

    def get_all_reponame(self):
        # Returns a list of repos associated with GitHub account
        names = list()

        for repo in self._g.get_user().get_repos():
            names.append(repo.full_name)

        return names

    def get_user(self):
        # Return user name of associated GitHub account
        r = self._g.get_user().name
        return r

    def get_user_id(self):
        # Return user id of associated GitHub account
        id = self._g.get_user().id
        return id

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

