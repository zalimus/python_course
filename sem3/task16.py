# Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

x = int(input("Введите количество элементов в массиве: "))

arr = []
for i in range(5):
    arr.append(randint(1, 10))

count = 0
for elem in arr:
    if elem == x:
        count += 1

print(f"Число {x} встречается в массиве {arr} {count} раз(а)")
