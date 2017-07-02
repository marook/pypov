class Include(object):
    def __init__(self, path=None):
        self.path = path

    def toPovray(self):
        return '#include "{}"'.format(self.path)
