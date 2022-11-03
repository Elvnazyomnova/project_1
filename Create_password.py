import random
from random import sample
sim = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
try:
   dlina = int(input('введите количество символов'))
except TypeError:
   print('Ошибка ввода длины пароля')
parol = sample(sim, dlina)
print('Пароль:', ''.join(parol))
