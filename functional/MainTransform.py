from functional import Transform

t = "Expected:{}           Given:{}                 Test:{}"


def run_map():
    input_list = [1, 2, 3, 4]
    expected_output = ['1', '2', '3', '4']
    print_result(expected_output, Transform.map(input_list, lambda x: str(x)))
    input_list = [1, 2, 3, 4]
    expected_output = ['1', '4', '9', '16']
    print_result(expected_output, Transform.map(input_list, lambda x: str(x ** 2)))


def run_filter():
    input_list = [i for i in range(100)]
    expected_output = [i for i in range(0, 100, 3)]
    print_result(expected_output, Transform.filter(input_list, lambda x: x % 3 == 0))

    input_list = [i for i in range(20)]
    expected_output = [0, 1, 2, 3, 5, 8, 13]
    print_result(expected_output, Transform.filter(input_list, lambda x: x in [0, 1, 2, 3, 5, 8, 13]))


def print_result(expected_output, output_object):
    print(t.format(format_list(expected_output),
                   format_list(output_object),
                   expected_output == output_object))


def format_list(l: list):
    if type(l) is int:
        return l
    if len(l) > 5:
        text = str(l[:2]) + str(l[-2:])
        text = text.replace('[', '').replace(']', '...', 1)
        return '[' + text
    return str(l)


class Obj:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    # run_map()
    run_filter()
    pass
