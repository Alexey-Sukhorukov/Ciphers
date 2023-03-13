# import binascii


# data = input('Введите текст для шифрования:\n> ')
# for i in data:
#     # j = binascii.hexlify(bytes(i, encoding='utf-8')).upper()
#     j = i.encode('utf-8')
#     print(bin(int(j.decode('utf-8'), 16))[2:].zfill(4), end=' ')
# # data_hex = binascii.hexlify(bytes(data, encoding='utf-8'))[1:].upper()
# print()
# data_bin = ''
# # print(' '.join(format(ord(x), 'b') for x in data))

# # print(bin(int('123', 16))[2:].zfill(5))