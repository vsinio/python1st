#print("hello world")

#a = 2
#b = 3.23
#c = "Hello"
#d = None
#f = True

#lst_a = [1,2,3] #список (int str и тд)
#print(a, (type(a))) #type(переменная) функция показывающая класс (int)
#print(b, (type(b))) float
#print(c, (type(c))) str
#print(d, (type(d))) none
#print(f, (type(f))) bool
#print(a,'-',b,'-',c)
#print('{0} - {1} - {2}'.format(a,b,c))  #применение форматированной строки, все по порядку(по индексам)
#print(f'{a} - {b} - {c}') #f строка
#print(f, (type(f)))
#print(lst_a)


#print("press a")
#a = int(input()) # input = always str, if u need int - a = int(input()), float - float(input())
#print('press b')
#b = int(input())
#print(f'a = {a}, b = {b}')
#c = a + b
#print(a, '+', b, '=', a+b)
#print(a, '+', b, '=', c)
#print(a+b)


# + - / // % * **
"""a = 15
b = 4
print(type(a/b)); print(a/b) #обычное деление(инты может во флот превратить)
print(a//4) #целочисленное деление (15 / 4 = 3)
print(a%b) #остаток от деления 15 % 4 = 3
print(a**b) #** = возведение в степень = 15^4"""

"""a = 1.333
b = 3
c = (a * b)
print(c) # 3.900000000004 ~ поэтому надо делать округление, round
#round по дефолту округляет к целым числам, пример: (в скобках указываем колво необходимых знаков (всего))
c = round(a*b, 3)
print(c) # = 4 """

'''a = 3 
a +=5 #a =  a + 5 аналогично и для других операций
print(a)'''

'''a = 1 > 4
print(a) # 1 > 4 = False, etc
a = 1 < 4 and 3 > 5
print(a)
a = 1 == 2 
print(a)
a = 1 != 4
print(a)

b = [1,2]
c = [1,2]
print(b == c) # True тк сравнение идет по элементно'''