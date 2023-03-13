from sympy import mod_inverse


# VдKкEоотFFLчк.тоU
# чужой ключ
alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
a, b = map(int, input('Введите параметры кода а и b через пробел: ').split())
m = 64
a1 = mod_inverse(a, m)

inp = list(input('Введите сообщение для дешифрования: '))
# inp = 'рPCPьчVуррDчVбCPчLу?ч?ц'
data = [alphabet[i] for i in inp]
data_y = list(map(lambda x: a1 * (x + m - b), data))
data_mod = list(map(lambda x: x % m, data_y))
print('data: ', *data, sep='\t')
print('data_y: ', *data_y, sep='\t')
print('data_mod: ', *data_mod, sep='\t')
decipher = []
for i in data_mod:
    for j in alphabet:
        if alphabet[j] == i:
            decipher.append(j)
            break

print('Результат декодирования:\t', *decipher, sep='')


# # fin = datetime.now()

# # print(f'Время работы программы{fin - st}')


# # Определение количества различных букв в закрытом тексте
# # st = 'рPCPьчVуррDчVбCPчLу?ч?ц'
# # q = {}
# # for i in st:
# #     if i not in q:
# #         q[i] = 1
# #     else:
# #         q[i] += 1
# # print(q)

# # Определение возможных комбинаций a и b
# # for a in range(3, 100, 2):
# #     for b in range(1, 64):
# #         if 13 * a + b <= 127 and (13 * a + b) % 64 == 15:
# #             print(a, b)
# #
# # for a in range(3, 100, 2):
# #     for b in range(1, 64):
# #         if 13 * a + b < = 127 and (13 * a + b) % 64 == 42:
# #             print(a, b)


