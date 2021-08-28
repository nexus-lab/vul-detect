# utility.py
"""
    Collection of functions needed as utility
"""

import os  # OS interaction
import stat  # File attributes
import shutil  # File usage


def write_change(func, path, info):
    """
    Method handing write permission issues

    :param func: function of issue, string
    :param path: path to file, string
    :param info: info of issue, string
    """
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def clear_temp():
    """
    Method to clear temp folder
    """
    # TODO: Fix
    path = os.getcwd() + '/temp/'

    try:
        shutil.rmtree(path, ignore_errors=True)
        shutil.rmtree(path, onerror=write_change)
    except Exception as e:
        print(e, 'Trying second strategy')
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(e)


def return_path():
    """
    Utility method to current directory path

    :return: current working directory, string
    """
    return os.getcwd()
