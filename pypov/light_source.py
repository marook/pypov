import props

class LightSource(object):
    POV_NAME = 'light_source'
    
    POV_ARGS = [
        'location',
    ]

    POV_EXTRA_ARGS_SEPARATOR = True
    
    POV_MODIFIERS = [
        'color',
        'point_at',
        'parallel',
    ]
    
    def __init__(self, location):
        self.location = location
        props.apply_pov_properties(self)
