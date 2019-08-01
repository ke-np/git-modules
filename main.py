from datetime import datetime

from core.utils import calculator, misc

def printFormatter(name):
    def wrapper(f):
        def decorated_func(*args, **kwargs):
            border_length = 42
            print('\n')
            print('+'*border_length)
            print(name)
            print('+'*border_length)

            f(*args, **kwargs)

            print('+'*border_length)

        return decorated_func
    return wrapper

@printFormatter('CALCULATOR')
def do_math():
    
    a = 100
    b = 25

    print('a = {}, b = {}'.format(a, b))

    print('a + b = {}'.format(calculator.add(a, b)))
    print('a - b = {}'.format(calculator.substract(a, b)))
    print('a * b = {}'.format(calculator.multiple(a, b)))
    print('a / b = {}'.format(calculator.divide(a, b)))


@printFormatter('MISC')
def do_misc_utils():
    print('Random number: {}'.format(misc.rand()))
    print('Random password: {}'.format(misc.generate_password()))


print('Hello, Time is: {}'.format(datetime.utcnow()))

do_math()
do_misc_utils()


