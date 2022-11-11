import time
from cryptography.fernet import Fernet

#starting timer
start = time.perf_counter()

key = Fernet.generate_key()
f = Fernet(key)

#opening image and assigning bytes to token var
with open('/Users/emmanuelhuitron/Desktop/Test/motorCycle.cr2', 'rb') as originalFile:
    token = originalFile.read()

encrypted = f.encrypt(token)

#writing encrypted image file
with open ('/Users/emmanuelhuitron/Desktop/Test/encImage.cr2', 'wb') as encryptedFile:
    encryptedFile.write(encrypted)

middle = time.perf_counter()
print(f'Finished encryption in {round(middle-start, 2)} second(s)')

with open('/Users/emmanuelhuitron/Desktop/Test/encImage.cr2', 'rb') as encryptedFile:
    encrypted = encryptedFile.read()

decrypted = f.decrypt(encrypted)

with open('/Users/emmanuelhuitron/Desktop/Test/decImage.cr2', 'wb') as decryptedFile:
    decryptedFile.write(decrypted)

finish = time.perf_counter()
print(f'Finished overall in {round(finish-start, 2)} second(s)')
