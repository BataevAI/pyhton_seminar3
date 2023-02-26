# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
from math import *
list_1 = []
print("Введите размер массива")
n = int(input())
print("Введите диапазоны массива")
left = int(input())
right = int(input())
print(f"Введите число Х [{left}; {right}], которое будем искать в массиве")

# метод создания списка случайных элементов с границами - left и right

def randList(n, left1, right1):
    list_1 = []
    for i in range(n):
        t = randint(left1, right1)         
        list_1.append(t)  
    print(*list_1)
    return list_1


list_2 = randList(n, left, right)
# # search - наше искомое число в списке
search = list_2[0]
# searchNum - вводимое число, ближайшее к которому мы ищем
searchNum = int(input())   
delta = 0

for i in range(0, n - 1):
    # print(f'i = : {i}')    
    # print(f'search : {search}') 
  
    if list_2[i] == searchNum: 
        search = list_2[i]
        break
    else:
           
        if (abs(list_2[i + 1] - searchNum)) <= abs(search - searchNum):            
            search = list_2[i + 1]    

print(f'Искомое число: {search}')  