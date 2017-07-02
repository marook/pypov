def povlify(obj):
    if(isinstance(obj, tuple)):
        return vectorify(obj)
    elif(isinstance(obj, str)):
        return obj
    elif(isinstance(obj, float)):
        return str(obj)
    elif(hasattr(obj, 'povlify')):
        return obj.povlify
    elif(is_element(obj)):
        return elementify(obj)
    else:
        raise Exception('Can\'t convert type {} to povray'.format(type(obj)))

def vectorify(vec):
    return '<{}>'.format(', '.join([str(x) for x in vec]))

def is_element(obj):
    t = type(obj)
    return hasattr(t, 'POV_NAME')

def elementify(e):
    t = type(e)
    lines = [
        '{} {{'.format(t.POV_NAME),
    ]
    if(hasattr(t, 'POV_ARGS')):
        lines.append(', '.join([povlify(getattr(e, key)) for key in t.POV_ARGS if not getattr(e, key) is None]))
    if(hasattr(t, 'POV_EXTRA_ARGS_SEPARATOR')):
        lines.append(',')
    if(hasattr(t, 'POV_MODIFIERS')):
        for key in t.POV_MODIFIERS:
            value = getattr(e, key)
            if(not value is None):
                lines.append('{} {}'.format(key, povlify(value)))
    lines.append('}')
    return '\n'.join(lines)
