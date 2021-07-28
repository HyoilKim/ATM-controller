class AuthException(Exception):
    def __str__(self):
        return 'Not allowed auth'

class NotAllowedActionException(Exception):
    def __str__(self):
        return 'Not allowed action'