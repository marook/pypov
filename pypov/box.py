import props

class Box(object):
    POV_NAME = 'box'
    
    POV_ARGS = [
        'corner_1',
        'corner_2',
    ]

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self, corner_1, corner_2):
        self.corner_1 = corner_1
        self.corner_2 = corner_2
        props.apply_pov_properties(self)
