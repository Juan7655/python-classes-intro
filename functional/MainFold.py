from functional import PolymorphicFunctions, FibonacciTail, Fold

t = "Expected:{}           Given:{}                 Test:{}"


def run_fibonacci_tail():
    print_result(expected_output=0, output_object=FibonacciTail.of(0))
    print_result(expected_output=1, output_object=FibonacciTail.of(1))
    print_result(expected_output=1, output_object=FibonacciTail.of(2))
    print_result(expected_output=2, output_object=FibonacciTail.of(3))
    print_result(expected_output=13, output_object=FibonacciTail.of(7))
    print_result(expected_output=2971215073, output_object=FibonacciTail.of(47))

    # print(FibonacciTail.of(-1))  # ValueError


def run_composition():
    i = lambda x: x + 1
    h = lambda x: x ** 2
    g = lambda x: x - 5
    f = lambda x: 10 * x

    c = PolymorphicFunctions.multi_compose(f, g, h, i)

    print_result(expected_output=-40, output_object=c(0))
    print_result(expected_output=1160, output_object=c(10))


def run_partial_application():
    f = lambda x, y: x + y
    partial = PolymorphicFunctions.partial_application(f, 5)

    print_result(expected_output=9, output_object=partial(4))


def run_fold_right():
    input_list = [5, 8, 7, 6]

    print_result(expected_output=26, output_object=Fold.suma_right(input_list))
    print_result(expected_output=1680, output_object=Fold.producto_right(input_list))
    print_result(expected_output=[], output_object=Fold.right(input_list, None, lambda x, y: []))

    input_list = [i for i in range(80)]
    print_result(expected_output=80, output_object=Fold.length_of_list_right(input_list))


def run_fold_left():
    input_list = [5, 8, 7, 6]

    print_result(expected_output=26, output_object=Fold.suma_left(input_list))
    print_result(expected_output=1680, output_object=Fold.producto_left(input_list))
    print_result(expected_output=[], output_object=Fold.left(input_list, None, lambda x, y: []))

    input_list = [i for i in range(80)]
    expected_output = 80
    print_result(expected_output, Fold.length_of_list_left(input_list))


def run_reverse_list():
    input_list = [1, 2, 3, 4]
    expected_output = [4, 3, 2, 1]
    print_result(expected_output, Fold.reverse(input_list))

    input_list = [i for i in range(100)]
    expected_output = [99 - i for i in range(100)]
    print_result(expected_output, Fold.reverse(input_list))


def run_reverse_list_right():
    input_list = [1, 2, 3, 4]
    expected_output = [4, 3, 2, 1]
    print_result(expected_output, Fold.reverse_right(input_list))

    input_list = [i for i in range(100)]
    expected_output = [99 - i for i in range(100)]
    print_result(expected_output, Fold.reverse_right(input_list))


def run_list_of_lists():
    input_list = [[i for i in range(20)] for _ in range(10)]
    expected_output = [i for i in range(20)] * 10

    print_result(expected_output, Fold.list_of_lists(input_list))


def run_sum_1():
    input_list = [i for i in range(20)]
    expected_output = [i + 1 for i in range(20)]

    print_result(expected_output, Fold.sum_1(input_list))


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


if __name__ == "__main__":
    # run_sum_1()
    # run_list_of_lists()
    # run_reverse_list_right()
    # run_reverse_list()
    # run_fold_left()
    # run_fold_right()
    # run_partial_application()
    # run_composition()
    run_fibonacci_tail()
    pass
