from math import*

a = int(input('Введите значение A ='))
b = int(input('Введите значение B ='))
counter = 0
print('___________')
for i in range(a, b+1):
	print(i, end=" ")
	counter+=1
print('')
print('Количество чисел: ', counter)