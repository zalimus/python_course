# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.


def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

print(f"{a} в степени {b} равно {power_recursive(a, b)}")