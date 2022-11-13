import time
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
print("Key: ", key)

filesPath = input("Please enter directory of desired files: ")
dirList = os.listdir(filesPath)
encFilePath = "/Users/emmanuelhuitron/Desktop/Encrypted"
decFilePath = "/Users/emmanuelhuitron/Desktop/Decrypted"

#starting timer
start = time.perf_counter()

i = 0
while i < len(dirList):
    #opening image and assigning bytes to token var
    with open(filesPath + "/" + dirList[i], 'rb') as originalFile:
        token = originalFile.read()

    encrypted = f.encrypt(token)

    #writing encrypted image file
    with open (encFilePath + "/img" + str(i) + ".ARW", 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
    print("Encrypted file ", i)
    i += 1

middle = time.perf_counter()
print(f'***Finished encryption in {round(middle-start, 2)} second(s)***')

dirList = os.listdir(encFilePath)
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
