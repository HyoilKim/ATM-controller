class AuthException(Exception):
    def __str__(self):
        return 'Not allowed auth'

class ActionException(Exception):
    def __str__(self):
        return 'Not allowed action'