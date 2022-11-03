#4 раза бросается 6-сторонний кубик, выводится сумма бросков.
from random import sample
i = 0
arr = []
cub = range(1,6)
total = 0
while i != 4:
    throw = sample(cub, 1)
    arr.append(throw)
    i += 1
    print(f'Бросок {i}, выпавшее число {throw}')
for k in arr:
    total += i
print(f'Сумма бросков: {total}')
