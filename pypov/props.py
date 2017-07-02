def apply_pov_properties(obj):
    t = type(obj)
    for key in t.POV_ARGS + t.POV_MODIFIERS:
        if(not hasattr(obj, key)):
            setattr(obj, key, None)

OBJECT_MODIFIERS = [
    'pigment',
    'texture',
    'materiat',
    'normal',
]
