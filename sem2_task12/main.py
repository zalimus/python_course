# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя 
# делает две подсказки. Он называет сумму этих чисел S и их 
# произведение P. Помогите Кате отгадать задуманные Петей числа.


import math

s = int(input("Введите сумму чисел S: "))
p = int(input("Введите произведение чисел P: "))


x = (s - math.sqrt(s**2 - 4*p)) / 2
y = (s + math.sqrt(s**2 - 4*p)) / 2

x = int(x)
y = int(y)

print(f"Натуральные числа X и Y {x, y}")