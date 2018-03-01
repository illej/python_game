from main import *


def test():
    """
    >>> round_float(1.1)
    1
    >>> round_float(1.5)
    2
    >>> round_float(1.6)
    2
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    test()
