

def new_random_lst(x): #ввод количества элементов в списке
    from random import randint
    len_lst = x
    lst = []
    for i in range(len_lst):
        lst.append(randint(0, 10))
    return lst


print(new_random_lst(6))

lst = new_random_lst(6)
print(lst)
