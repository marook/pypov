class Camera(object):
    def __init__(self):
        self.camera_type = None
        self.camera_vector = None
        self.location = None
        self.look_at = None

    @property
    def pov(self):
        lines = [
            'camera {',
        ]
        for key in ['location', 'look_at']:
            value = getattr(self, key)
            if(not value is None):
                lines.append('{} {}'.format(key, value.pov))
        lines.append('}')
        return '\n'.join(lines)
