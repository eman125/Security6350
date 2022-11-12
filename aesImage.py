import time
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

fileName = input("Please enter path of desired file: ")
fileExt = input("Enter file extension without a .  ie: jpeg ")

#starting timer
start = time.perf_counter()

#opening image and assigning bytes to token var
with open(fileName, 'rb') as originalFile:
    token = originalFile.read()

encrypted = f.encrypt(token)

#writing encrypted image file
with open ('/Users/emmanuelhuitron/Desktop/Test/encFile.txt', 'wb') as encryptedFile:
    encryptedFile.write(encrypted)

middle = time.perf_counter()
print(f'Finished encryption in {round(middle-start, 2)} second(s)')

with open('/Users/emmanuelhuitron/Desktop/Test/encFile.txt', 'rb') as encryptedFile:
    encrypted = encryptedFile.read()

decrypted = f.decrypt(encrypted)

with open('/Users/emmanuelhuitron/Desktop/Test/decImages.' + fileExt, 'wb') as decryptedFile:
    decryptedFile.write(decrypted)

finish = time.perf_counter()
print(f'Finished overall in {round(finish-start, 2)} second(s)')
