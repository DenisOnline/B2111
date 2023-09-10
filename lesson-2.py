# def fist_function():
#     pass
#
#
# def hello_world():
#     hello = "Hello World!"
#     return hello
#
#
# def summ(x, y):
#     return x + y
#
#
# def fun(a, b, c=2):
#     return a + 4 * b / 2 + c ** 2
#
#
# def add(count, list1=[]):
#     list1.append(count)
#     return list1
#
#
# a = add(34)
# print(a)
# b = add(346)
# print(b)
# print(a is b)
# str1 = "1234"
# str2 = str1
# print(str1)
# print(str2)
# str1 = "4321"
# print(str1)
# print(str2)
# print(fist_function())
# print(hello_world())
# print(summ(23, 45))
# print(summ("X", "Y"))
# print(summ(input(), input()))
# print(summ(int(input()), int(input())))
# print(summ(x=1, y=4))
# print(fun(2, 5))
#
from random import randint
from time import sleep

def coin_simulator():
    number = randint(0,1)
    print('Бросаю монетку')
    sleep(1)

    if number ==0:
        return'Орёл'
    else:
        return 'Решка'

print(coin_simulator())