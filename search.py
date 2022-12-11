#jump searsch
import math
from random import randint

def JumpSearch (arr, value):
  length = len(arr) # Длинна массива
  jump = int(math.sqrt(length)) # Размер прыжка
  left = 0
  right = 0
  while left < length and arr[left] <= value:
    right = min(length - 1, left + jump)
    if arr[left] <= value and arr[right] >= value:
      break
    left += jump
  if left >= length or arr[left] > value:
    return -1
  right = min(length - 1, right)
  i = left 
  while i <= right and arr[i] <= value:
    if arr[i] == value:
      return i
    i += 1
  return - 1

testarr = []
for i in range(15):
  testarr.append(randint(50, 150))
  testarr.sort()
print (testarr)
x = int(input('Введи число'))

if JumpSearch(testarr, x) != -1:
  print ("Элемент под индексом", JumpSearch(testarr,x))
else:
  print ("Элемент отсутствует в массиве")
  
#Interpolation Search
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
