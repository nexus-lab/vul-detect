#Scanner.py
"""
    Scanner class - will contain functions conducting vulnerability scans
"""

import subprocess  # Application handling

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
        # output = subprocess.getoutput('flawfinder --csv ' + self.path)
        # print(output)

    def gitrob_scan(self):
        # TODO: Implement gitrob
        pass

    def truffleHog_scan(self):
        # TODO: Implement truffleHog
        pass

