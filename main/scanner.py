#scanner.py
"""
    Scanner class - will contain functions conducting vulnerability scans
"""

import subprocess  # Application handling


class scanner:
    # TODO: Needs better implementation of scan tools

    def __init__(self, path):
        # Must instantiate an operating path for scanner to operate
        # TODO: Add automatic install of missing tools
        self.path = path

    def bandit_scan(self):
        # Static python source code vulnerability analysis
        subprocess.call(["bandit", "-r", self.path, "-f", "csv", "-o", self.path + "\\scanresultspy.csv"])

    def flawfinder_scan(self):
        # Static C/C++ source code vulnerability analysis
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

