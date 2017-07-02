import props

class Plane(object):
    POV_NAME = 'plane'
    
    POV_ARGS = [
        'plane_normal',
        'distance',
    ]

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self, plane_normal, distance):
        self.plane_normal = plane_normal
        self.distance = distance
        props.apply_pov_properties(self)
