import numpy as np

alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
alphabet_reverse = dict(zip(list(range(64)), list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?')))

# alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
# alphabet_reverse = dict(zip(list(range(61)), list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.')))

# inp = list(input('Введите сообщения для шифрования: '))

open_text = 'HERE IS A LITTLE LESSON IN TRICKERY '
key = 'эбяирAьщ рхTAлцZ'
data_vector = [alphabet[i] for i in open_text]
key_vector = [alphabet[i] for i in key]

# размерность ключа матрицы
n = int(len(key) ** 0.5)

key_matrix = np.array(key_vector).reshape((n, n)) 

data_matrix = np.array(data_vector).reshape((len(data_vector) // n, n))
print(data_vector)
print('Ключ-матрица:\n',key_matrix, '\n')
print('Открытый текст ввиде матрицы-значений:\n', data_matrix, '\n')

close_text = []
for i in data_matrix:
    res = np.dot(i, key_matrix) % len(alphabet)
    print(res)
    close_text.extend([alphabet_reverse[i] for i in list(res)])

print('Зашифрованный текст: ',*close_text,'\n', sep='')