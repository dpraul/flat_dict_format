
class FDFException(Exception):
    """ This exception occurred somewhere in the FDF codebase """


class BadDelimiterException(FDFException):
    """ The dict delimiter isn't in this line and needs to be. """

__all__ = [BadDelimiterException, FDFException]
