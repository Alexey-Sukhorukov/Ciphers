import rsa
(pubkey, privkey) = rsa.newkeys(911)
print(f'\nОткрытый ключ: {pubkey}\n\nЗакрытый ключ: {privkey}\n')
 
message = bytes(input('Введите сообщение для шифрования: '), encoding = 'utf-8')
print(message)
# шифруем
# crypto = rsa.encrypt(message, pubkey)
# print('\n\nЗашифрованное сообщение: ', crypto, '\n')
# #расшифровываем
# message = rsa.decrypt(crypto, privkey)
# print('Дешифрованное сообщение: ', message, '\n')