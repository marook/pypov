import props

class Union(object):
    POV_NAME = 'union'
    
    POV_MANY_ARG = 'objects'

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self):
        props.apply_pov_properties(self)
