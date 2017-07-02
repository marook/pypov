class Sphere(object):
    POV_NAME = 'sphere'
    
    POV_ARGS = [
        'center',
        'radius',
    ]

    POV_MODIFIERS = [
        'pigment',
    ]
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.pigment = None
