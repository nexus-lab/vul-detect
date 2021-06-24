#Scanner.py
"""
    Scanner class - will contain functions conducting vulnerability scans
"""

import subprocess  # Application handling
import os # Directory navigation

class Scanner:
    # TODO: Needs better implementation of scan tools

    def __init__(self, path):
        # Must instantiate an operating path for scanner to operate
        # TODO: Add automatic install of missing tools


        self.path = path

    def bandit_scan(self):
        # Static python source code vulnerability analysis
        try:
            subprocess.call(['bandit', '--version'])
        except FileNotFoundError:
            raise FileNotFoundError("Bandit is not installed on this system.")
        subprocess.call(["bandit", "-r", self.path, "-f", "csv", "-o", self.path + "\\scanresultspy.csv"])

    def flawfinder_scan(self):
        # Static C/C++ source code vulnerability analysis
        try:
            subprocess.call(['flawfinder', '--version'])
        except FileNotFoundError:
            raise FileNotFoundError("FlawFinder is not installed on this system.")
        out = open(self.path + "\\test.csv", "w")
        subprocess.call(["flawfinder", "--csv", self.path], stdout=out)
        out.close()

    def trufflehog_scan(self, url):
        # GitHub ENTROPY/REGEX SECRET scans
        # NOTE: Line 381 in trufflehog.py contains a bug disallowing proper usage on windows systems.
        # TODO: Implement trufflehog to scan ALREADY cloned repos
        out = open(os.getcwd() + "/temp/this.json", "w")
        subprocess.call(["trufflehog", "--json", url], stdout=out)
        out.close()

    def gitleaks_scan(self):
        # GitHub secret scanning - requires standalone executable
        subprocess.call(["gitleaks", "--path=" + self.path, "--report=" + os.getcwd() + "/temp/other.json"])

