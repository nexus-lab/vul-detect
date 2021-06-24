# utility.py
"""
    Collection of functions needed as utility
"""

import os  # OS interaction
import stat  # File attributes
import shutil  # File usage


def write_change(func, path, info):
    # Handling write path issues when deleting files
    # Utility method
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def clear_temp():
    # Utility method, will clear temp folder
    path = os.getcwd() + '/temp/'

    try:
        shutil.rmtree(path, ignore_errors=True)
        shutil.rmtree(path, onerror=write_change)
    except shutil.Error as e:
        print(e, 'Trying second strategy')
        try:
            shutil.rmtree(path)
        except shutil.Error as e:
            print(e)


def return_path():
    # Utility method to current directory path
    return os.getcwd()
