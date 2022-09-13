#R/L = 2*pi*R
#S = pi * R**2

from math import*

r = float(input('Введите значение R ='))

S = pi * r**2
L = r/(2*pi*r)

print(f'S ={S:.2f}, L ={L:.2f}')