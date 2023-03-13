from sympy import mod_inverse
from datetime import datetime

# st = datetime.now()
alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))

# inp = 'RGвуREбDJRчWоMFTчKNCеVаXу'
# inp = 'WJVпдLKе:XUMьFXMPпбCPYVBгZьSUJIпбLAпGAYDьXгMPB'
inp = list(input('Введите сообщения для шифрования: '))
# inp = list('крипто')
# KEY
key = list(input('Введите ключ для шифрования: '))
print()
# key = list('KEY')

l = len(key)
for i in range(l, len(inp)):
    key.append(key[i % l])
    
print('Буква открытого текста:    ', *inp, sep='\t')
print('Буква ключа:','\t',  *key, sep='\t')

data_x = ['0' * (6 - len(bin(alphabet[i])[2:])) + bin(alphabet[i])[2:] for i in inp]
data_y = ['0' * (6 - len(bin(alphabet[j])[2:])) + bin(alphabet[j])[2:] for j in key]

print('x:', '\t'*2, *data_x, sep='\t')
print('y:', '\t'*2, *data_y, sep='\t')

res = []
for i, j in zip(data_x, data_y):
    q = [ord(z)^ord(x) for z, x in zip(i, j)]
    # print(q)
    res.append(int((''.join(map(str, q))), base=2))

print('xor(x, y) в десятич. сиcтеме:',  *res, '\n', sep='\t')

cipher = []
for i in res:
    for j in alphabet:
        if alphabet[j] == i:
            cipher.append(j)
            break

print('Результат кодирования:    ', *cipher, sep='')

# щ - и   ы   х   д   и   э   о   ц       и   C   л   б   ?   ь   ж   C   я   !   ч   т   м   п   к   д
# э - м   ч   с   а   м   щ   т   ъ   !   м   G   з   е   ,   ш   к   G   :       ы   о   и   у   ж   а
# с -     у   э   G       х   ц   о   и       а   :   D   н   ф   ю   а   з   м   п   ъ   !   ч   .   G


# W   J   V   п   д   L   K | е   :   X   U   M   ь   F | X   M   P   п   б   C   P | Y   V
# B   г   Z   ь   S   U   J   I   п   б   L   A   п   G   A   Y   D   ь   X   г   M   P   B