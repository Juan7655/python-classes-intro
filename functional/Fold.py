def right(l: list, identity, f):
    if l is None or len(l) == 0:
        return identity
    else:
        return f(l[0], right(l[1:], identity, f))


def left(l: list, identity, f, acc=None):
    if acc is None:
        acc = identity
    if l is None or len(l) == 0:
        return acc
    else:
        return left(l[:-1], identity, f, f(acc, l[-1]))


def suma_right(l: list):
    return right(l, 0, lambda x, y: x + y)


def producto_right(l: list):
    return right(l, 1, lambda x, y: x * y)


def suma_left(l: list):
    return left(l, 0, lambda x, y: x + y)


def producto_left(l: list):
    return left(l, 1, lambda x, y: x * y)


def reverse(l: list):
    return left(l, [], lambda x, y: x.append(y))


def length_of_list_left(l: list):
    return left(l, 0, lambda x, y: x + 1)


def length_of_list_right(l: list):
    return right(l, 0, lambda x, y: 1 + y)


def sum_1(l: list):
    return left(l, [], lambda x, y: [y + 1] + x)


def reverse_right(l: list):
    return right(l, [], lambda x, y: y + [x])


def list_of_lists(l: list):
    return left(l, [], lambda x, y: x + y)
