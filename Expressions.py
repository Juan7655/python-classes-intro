def run():
    var = ()  # yields empty tuple - inmutable
    a, b = 5, 4  # tuples are not formed with parenthesis, but with comma operator

    # calls()

    # lists_sets()

    a = [i for i in range(100)]
    print(a)


def calls():
    f(a=1, b=0)
    f(b=1, a=0)
    f(b=1, *(2,))
    # f(1, b=2)
    # f(a=1, *(2,))
    f(1, *(2,))


def f(a, b):
    print(a, b)


def lists_sets():
    # Lists, Sets, Dictionaries
    explicit_list = [1, 2, 3, 4]
    comprehension_list = [i ** 2 for i in explicit_list]
    comprehension_list_2 = [x * y for x in range(10) for y in range(x, x + 10)]  # left to right evaluation

    set_display = {1, 2, 3, 4}  # mutable set object
    not_set = {}  # constructs an empty dictionary, not a set

    dictionary = {'a': 1, 'b': [1, 2, 3], 3: 'c'}
    dictionary_2 = {'a': 1, 'b': 1, 3: 'c'}
    comprehension_dictionary = {v: k for k, v in dictionary_2.items()}

    gen = generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))


def generator():  # returns an iterator called generator
    for i in [1, 2, 3, 4, 5]:
        yield i  # here it is suspended (local state retained)


if __name__ == "__main__":
    run()
