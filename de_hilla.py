import numpy as np
from sympy import mod_inverse

close_text = 'DбGзаъIMCьBнчйCEтжYщвряP!б.QсRэ W!Cг'
key = 'эбяирAьщ рхTAлцZ'

alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
alphabet_reverse = dict(zip(list(range(64)), list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?')))
print(len(alphabet))
key_vector = [alphabet[i] for i in key]
data_vector = [alphabet[i] for i in close_text]

# размерность ключа матрицы
n = int(len(key) ** 0.5)

key_matrix = np.array(key_vector).reshape((n, n))
data_matrix = np.array(data_vector).reshape((len(close_text) // n, n))

det = round(np.linalg.det(key_matrix))

print(det)
print(key_matrix)
print(mod_inverse(det, len(alphabet)))

key_inv = np.linalg.inv(key_matrix) * det

key_inv = np.around(key_inv)

key_inv = key_inv.astype('int')

key_inv = (key_inv * mod_inverse(det, len(alphabet))) % len(alphabet)

print(key_inv)

open_text = []
for i in data_matrix:
    res = np.dot(i, key_inv) % len(alphabet)
    print(res)
    open_text.extend([alphabet_reverse[int(i)] for i in res])


print(*open_text, sep='')