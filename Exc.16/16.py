# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# Последняя строка содержит число X
# # *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
list_1 = []
print("Введите размер массива")
n = int(input())
left = 1
right = 10
print(f"Введите число Х [{left}; {right}], которое будем искать в массиве")
searchNum = int(input())
count = 0
for _ in range(n):
    t = randint(left, right)    
    if t == searchNum: count = count + 1
    list_1.append(t)  
print(*list_1) 
print(f'В данном массиве X = {searchNum} содержится: {count} раз')   