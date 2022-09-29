#y = a*x**2 + cos(2*x+1)#

from math import *

a = float(input('Введите значение a ='))
x = float(input('Введите значение x ='))

y = a*x**2 + cos(2*x + 1)

print(f'y = {y:.2f}')

#f'y = (y:.2f)'#