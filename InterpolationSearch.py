import random
from random import randint

def InterpolationSearch(arr, value):
    low = 0
    high = (len(arr) - 1)
    while low <= high and value >= arr[low] and value <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (value - arr[low])))
        if arr[index] == value:
            return index
        if arr[index] < value:
            low = index + 1
        else:
            high = index - 1
    return -1
testarr = []
for i in range(10):
    testarr.append(randint(1, 100))
    testarr.sort()
print(testarr)
x = int(input('Введи число:'))
if InterpolationSearch(testarr,x) != -1:
    print ("Элемент найден в массиве, под индексом:,", InterpolationSearch(testarr,x))
else:
    print ("Элемент не найден в массиве")
