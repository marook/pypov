def apply_pov_properties(obj):
    t = type(obj)
    keys = (t.POV_ARGS if hasattr(t, 'POV_ARGS') else []) + t.POV_MODIFIERS
    for key in keys:
        if(not hasattr(obj, key)):
            setattr(obj, key, None)
    if(hasattr(t, 'POV_MANY_ARG')):
        if(not hasattr(obj, t.POV_MANY_ARG)):
            setattr(obj, t.POV_MANY_ARG, [])

TRANSPOSE_MODIFIERS = [
    'translate',
    'scale',
    'rotate',
]

OBJECT_MODIFIERS = [
    'pigment',
    'texture',
    'materiat',
    'normal',
    'finish',
] + TRANSPOSE_MODIFIERS
