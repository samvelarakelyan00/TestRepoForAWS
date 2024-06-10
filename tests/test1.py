def tests(f):
    if not f(1, 2) == 3:
        raise ValueError("Test1 failed!")
    if not f(1, 3.14) == 4.14:
        raise ValueError("Test2 failed!")
