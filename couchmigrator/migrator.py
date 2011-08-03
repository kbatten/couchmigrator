class Reader(object):
    def __init__(self, fp):
        pass

    def __iter__(self):
        return self

    def next(self):
        raise NotImplementedError

class Writer(object):
    def __init__(self, fp):
        pass

    def write(self):
        raise NotImplementedError
