class V(object):
    def __init__(self, *values):
        self.values = values

    @property
    def pov(self):
        return '<{}>'.format(', '.join([str(v) for v in self.values]))
