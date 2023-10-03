from random import randint

print("Введите кол-во чисел:")
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
print(a)

print("В каком порядке сортировать: 0 - Возрастание, 1 - Убывание")
var = int(input())

if(var == 0):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
else:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

print(a)