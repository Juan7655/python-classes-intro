from functional import Fold


def map(l: list, f):
    return Fold.left(l, [], lambda x, y: [f(y)] + x)


def filter(l: list, f):
    if len(l) == 0:
        return []
    elif len(l) == 1:
        return [l[0]] if f(l[0]) else []
    return ([l[0]] if f(l[0]) else []) + filter(l[1:], f)
