# vulErrors.py
"""
    Module containing custom exceptions for vulDetect
"""


class githInteractException(Exception):
    """Base class for githInteract exceptions"""
    pass


class TokenError(githInteractException):
    """Exception raised when incorrect token supplied.

    Attributes:
        Error -- original error that caused exception
        Message -- default supplied message
    """

    def __init__(self, *args):
        if args:
            self.error = str(args)
        else:
            self.error = None

    def __str__(self):
        if self.error:
            return 'Improper token. Original error: ' + self.error
        else:
            return 'Improper token/Input error'


class PasswordUserError(githInteractException):
    """Exception raised when username or password fails.

    Attributes:
        Error -- original error that caused exception
        Message -- default supplied message
    """

    def __init__(self, *args):
        if args:
            self.error = str(args)
        else:
            self.error = None

    def __str__(self):
        if self.error:
            return 'Improper username or password. Original error: ' + self.error
        else:
            return 'Improper username or password/Input error'
