import props

class Object(object):
    POV_NAME = 'object'
    
    POV_ARGS = [
        'object_identifier',
    ]

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self, object_identifier):
        self.object_identifier = object_identifier
        props.apply_pov_properties(self)
