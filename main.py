from datetime import datetime

from utils import calculator
a = 100
b = 25
print('Hello, Time is: {}'.format(datetime.utcnow()))
print('a = {}, b = {}'.format(a, b))

print('a + b = {}'.format(calculator.add(a, b)))
print('a - b = {}'.format(calculator.substract(a, b)))
print('a * b = {}'.format(calculator.multiple(a, b)))
print('a / b = {}'.format(calculator.divide(a, b)))
