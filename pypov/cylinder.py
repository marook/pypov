import props

class Cylinder(object):
    POV_NAME = 'cylinder'
    
    POV_ARGS = [
        'base_point',
        'cap_point',
        'radius',
    ]

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self, base_point, cap_point, radius):
        self.base_point = base_point
        self.cap_point = cap_point
        self.radius = radius
        props.apply_pov_properties(self)
