from sympy import mod_inverse


a, b = map(int, input('Введите параметры кода а и b через пробел: ').split())
m = 64
a1 = mod_inverse(a, m)
alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))

inp = list(input('Введите сообщения для шифрования: '))

data = [alphabet[i] for i in inp]

data_x = list(map(lambda x: a * x + b, data))
data_mod = list(map(lambda x: x % m, data_x))

cipher = []
for i in data_mod:
    for j in alphabet:
        if alphabet[j] == i:
            cipher.append(j)
            break

print('data:', *data, sep='\t')
print('data_x:', *data_x, sep='\t')
print('data_mod:', *data_mod, sep='\t')
print('Результат кодирования:\t', *cipher, sep='')