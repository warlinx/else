import random
#Создадим список случайных чисел
mas = [random.randint(0, 100) for i in range(20)]
#Выведем его на экран
print(mas)
l = len(mas)
for i in range(l//2):
    mas[i], mas[l - 1 - i] = mas[l - 1 - i], mas[i]
print(mas)