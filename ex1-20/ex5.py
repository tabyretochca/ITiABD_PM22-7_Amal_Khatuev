from math import*
import sys

n = int(input('Введите натурально число n ='))
x = float(input('Введите значение x ='))
sm = 0

for i in range(1, n+1):
	sm += cos(x)**i/i
print(sm)