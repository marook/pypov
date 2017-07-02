class Camera(object):
    POV_NAME = 'camera'
    
    POV_ARGS = [
        'camera_type',
    ]
    
    POV_MODIFIERS = [
        'location',
        'look_at',
    ]
    
    def __init__(self):
        self.camera_type = None
        self.camera_vector = None
        self.location = None
        self.look_at = None
