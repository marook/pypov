import props

class Sphere(object):
    POV_NAME = 'sphere'
    
    POV_ARGS = [
        'center',
        'radius',
    ]

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        props.apply_pov_properties(self)
