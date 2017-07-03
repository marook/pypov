import props

class Pigment(object):
    POV_NAME = ''
    
    POV_ARGS = [
        'pigment_identifier',
        'pigment_type',
    ]

    POV_MODIFIERS = [
        'color',
        'quick_color',
    ] + props.TRANSPOSE_MODIFIERS
    
    def __init__(self):
        props.apply_pov_properties(self)
