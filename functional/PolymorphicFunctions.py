def curry(f):
    return lambda a: lambda b: f(a, b)


def curry2(f):
    return lambda a: lambda b, c: f(a, b, c)


def multicurry(f):
    return lambda a: lambda b: lambda c: f(a, b, c)


def uncurry(f):
    return lambda x, y: f(x)(y)


def compose(f, g):
    return lambda x: f(g(x))


def multi_compose(*args):
    if len(args) == 0:
        raise Exception
    elif len(args) == 1:
        return args[0]
    else:
        return compose(args[0], multi_compose(*args[1:]))


def partial_application(f, a):
    return lambda b: f(a, b)
