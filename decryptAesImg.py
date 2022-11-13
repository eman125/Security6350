import time
import os
from cryptography.fernet import Fernet

key = input("Please enter the secret key: ")
f = Fernet(key)

encFilePath = "/Users/emmanuelhuitron/Desktop/Encrypted"
decFilePath = "/Users/emmanuelhuitron/Desktop/Decrypted"
dirList = os.listdir(encFilePath)

#starting timer
start = time.perf_counter()

i = 0
while i < len(dirList):
    with open(encFilePath + "/" + dirList[i], 'rb') as encryptedFile:
        encrypted = encryptedFile.read()

    decrypted = f.decrypt(encrypted)

    with open(decFilePath + "/" + str(i) + ".ARW", 'wb') as decryptedFile:
        decryptedFile.write(decrypted)
    print("Decrypted file ", i)
    i += 1

finish = time.perf_counter()
print(f'***Finished overall in {round(finish-start, 2)} second(s)***')
