from povlify import povlify

class Scene(object):
    def __init__(self):
        self.elements = []

    @property
    def povlify(self):
        return '\n'.join([povlify(e) for e in self.elements])
