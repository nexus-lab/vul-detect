# scanner.py
"""
    Scanner class - contains methods conducting vulnerability scans
"""

import subprocess  # Application handling
import os  # Directory navigation


class Scanner:

    def __init__(self, path):
        # Must instantiate an operating path for scanner to operate
        if os.name == 'nt':
            os.environ["PYTHONUTF8"] = "1"
        self.path = path
        self.temp = os.getcwd() + '/temp'
        self.repo = self.path.split('/')[-1]

    def bandit_scan(self):
        # Static python source code vulnerability analysis
        try:
            subprocess.call(["bandit", "-r", self.path, "-f", "csv", "-o", self.temp + "/bandit" + self.repo + ".csv"],
                            stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            raise FileNotFoundError("Bandit is not installed on this system.")

    def flawfinder_scan(self):
        # Static C/C++ source code vulnerability analysis
        # TODO: Add checks for proper operation of flawfinder
        out = open(self.temp + "/flawfinder" + self.repo + ".csv", "w", encoding="utf-8")
        try:
            subprocess.call(["flawfinder", "--csv", self.path], stdout=out)
        except FileNotFoundError:
            raise FileNotFoundError("FlawFinder is not installed on this system.")
        out.close()

    def gitleaks_scan(self):
        # GitHub secret scanning - requires standalone executable
        try:
            subprocess.call(["gitleaks", "--path=" + self.path,
                             "--report=" + os.getcwd() + "/temp/gitleaks" + self.repo + ".json"],
                            stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            raise FileNotFoundError("Gitleaks is not installed on this system")
