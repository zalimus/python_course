# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

x = int(input("Введите число X: "))

arr = []
for i in range(5):
    arr.append(randint(1, 10))

print(arr)

min_diff = abs(x - arr[0])
closest_num = arr[0]

for elem in arr:
    diff = abs(x - elem)
    if diff < min_diff:
        min_diff = diff
        closest_num = elem

print("Самое близкое число к", x, "из массива", arr, "равно", closest_num)