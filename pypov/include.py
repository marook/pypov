class Include(object):
    def __init__(self, path=None):
        self.path = path

    @property
    def povlify(self):
        return '#include "{}"'.format(self.path)
