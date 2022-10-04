# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def lst_keyboard(x):  # создать список от -N до N
    len_n = -x
    lst = []
    for i in range(x*2+1):
        lst.append(len_n)
        len_n+=1
        
    return lst
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


N = int(input("Введите N: "))
lst = lst_keyboard(N)
lst_fibb = []

for i in lst:
    if lst[i] > 0:
        lst_fibb.append(fibonacci(lst[i]))

print(f"Первоначальный список = {lst}")
print(f"Список с числами Фибоначчи = {lst_fibb}")

