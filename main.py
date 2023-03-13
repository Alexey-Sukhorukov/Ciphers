import numpy as np
from itertools import product
from sympy import mod_inverse
import random

alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
alphabet_reverse = dict(zip(list(range(64)), list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?')))
s='ABCD EFGHIJKLMNOPQRSTUVWXYZ'
f = open('keys_for_hilla.txt', 'a', encoding='utf-8')
count = 0
while count < 25:
    key_matrix = np.random.randint(0, 64, size=(4, 4))
    det = round(np.linalg.det(key_matrix))

    if det < 0:
        continue
    try:
        mod_inverse(det, len(alphabet))
    except Exception:
        continue

    print(f'Определитель: {det}\nОбратный элемент {mod_inverse(det, len(alphabet))}\nМатрица:\n{key_matrix}\n')
    count += 1
    key = []
    for i in key_matrix:
        key.extend([alphabet_reverse[j] for j in i])
    print('Ключ: ', *key, '\n\n', sep='')
    f.write(''.join(key) + '\n')

f.close()