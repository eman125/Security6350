import time
import os
from cryptography.fernet import Fernet

key = input("plz gib key: ")
f = Fernet(key)
print("Key: ", key)

binVar = input("Encrypt(True) or decrypt(False)(case sensative)? ")

filesPath = input("Please enter directory of desired file: ")
encFilePath = "/Users/emmanuelhuitron/Desktop/Encrypted/myEnc.ARW"
decFilePath = "/Users/emmanuelhuitron/Desktop/Decrypted/myDec.ARW"

#starting timer
start = time.perf_counter()

if binVar == True:
    with open(filesPath, 'rb') as originalFile:
        token = originalFile.read()

    encrypted = f.encrypt(token)

    with open(encFilePath, 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
    print("encrypted the file.")
else:
    with open(filesPath, 'rb') as encryptedFile:
        encrypted = encryptedFile.read()

    decrypted = f.decrypt(encrypted)

    with  open(decFilePath, 'wb') as decryptedFile:
        decryptedFile.write(decrypted)
    print("Decrypted the file.")

finish = time.perf_counter()
print(f'***Finished overall in {round(finish-start, 2)} second(s)***')
