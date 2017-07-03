import props

class Intersection(object):
    POV_NAME = 'intersection'
    
    POV_MANY_ARG = 'objects'

    POV_MODIFIERS = props.OBJECT_MODIFIERS
    
    def __init__(self):
        props.apply_pov_properties(self)
