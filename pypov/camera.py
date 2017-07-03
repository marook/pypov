import props

class Camera(object):
    POV_NAME = 'camera'
    
    POV_ARGS = [
        'camera_type',
    ]
    
    POV_MODIFIERS = [
        'location',
        'look_at',
        'right',
        'up',
        'translate',
    ]
    
    def __init__(self):
        props.apply_pov_properties(self)
