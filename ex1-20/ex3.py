#a*x+1, x>=1
#a*x-1, x<0

from math import*

a = float(input('Введите значение a ='))
x = float(input('Введите значение x ='))

if x >=1:
	y=a*x+1
	print(f'y = {y:.2f}')
elif x<0:
	y=a*x-1
	print(f'y = {y:.2f}')
