@echo off
title Dependency Installation Windows - vul-detect
echo ENSURE PYTHON 3.9 or HIGHER IS INSTALLED - CLOSE AND INSTALL IF NOT
pause
pip install PyGithub
pip install pygit2
pip install bandit
pip install flawfinder
pip install trufflehog
