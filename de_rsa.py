import time

print(time.strftime('%X'))


n = 4391143
d = 3756007
# p, q = 509, 8627

alphabet = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюя ,.:!?'), list(range(64))))
alphabet_reverse = {alphabet[i] : i for i in alphabet}

inp = '823543 16384 1962374 16384 3297434 2097152 1851155 3297434 0 3297434 1922599 2097152 2469710 2469710 1922599 16384 3297434 1922599 16384 1851155 1851155 26072 1272515 3297434 2097152 1272515 3297434 2469710 1962374 2097152 128 1217714 16384 1962374 2118132'
close_text = map(int, inp.split())

decipher_mod = [pow(x, d, n) for x in close_text]

open_text = []
try:
    open_text = [alphabet_reverse[i] for i in decipher_mod]
    print('Расшифрованное сообщение: ', *open_text, sep='')
except KeyError:
    print('Ошибка расшифровки. Попробуйте ввести другой параметр d')

print(time.strftime('%X'))



# inp = map(int, list(input('Введите сообщения для расшифрования: ').split()))
# d = int(input('Введите параметр d: '))
