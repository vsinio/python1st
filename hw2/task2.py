#15.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

a = int(input("Введите число N: "))
lst = []

for i in range(1, a+1):
    lst.append(factorial(i))

print(f"факториалы от 1 до {a} = {lst}")