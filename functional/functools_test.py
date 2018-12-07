from functools import wraps, singledispatch


def run():
    fun("hola")
    fun(5)
    fun(8.0)
    print("-----------")
    temp()


@singledispatch
def fun(arg):
    print("Hello, world! " + arg)


@fun.register
def _(arg: int):
    print("I'm a number " + str(arg))


@fun.register
def _(arg: float):
    print("I'm a float " + str(arg))


def function_transmitter(f):
    @wraps(f)
    def wrapper():
        print('Applying first function')
        return f()
    return wrapper


def function_transmitter2(f):
    @wraps(f)
    def wrapper():
        print('Applying function')
        return f()
    return wrapper


@function_transmitter
def temp():
    print("this is my function")


if __name__ == "__main__":
    run()
