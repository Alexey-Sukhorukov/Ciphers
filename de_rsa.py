# p, q = 677, 911
n = 4391143

alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
# inp = map(int, list(input('Введите сообщения для расшифрования: ').split()))

inp = '823543 16384 1962374 16384 3297434 2097152 1851155 3297434 0 3297434 1922599 2097152 2469710 2469710 1922599 16384 3297434 1922599 16384 1851155 1851155 26072 1272515 3297434 2097152 1272515 3297434 2469710 1962374 2097152 128 1217714 16384 1962374 2118132'
inp = map(int, inp.split())
# d = int(input('Введите параметр d: '))
d = 3756007
decipher_mod = [x**d % n for x in inp]

decipher = []
for i in decipher_mod:
    if i not in alphabet.values():
        print('Ошибка расшифровки. Попробуйте ввести другой параметр d')
    for j in alphabet:
        if alphabet[j] == i:
            decipher.append(j)
            break
print('Расшифрованное сообщение: ', *decipher, sep='')