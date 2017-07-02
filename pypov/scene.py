
class Scene(object):
    def __init__(self):
        self.elements = []

    @property
    def pov(self):
        return '\n'.join([e.pov for e in self.elements])
