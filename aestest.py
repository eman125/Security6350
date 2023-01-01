import time
import os
import rmdot
from cryptography.fernet import Fernet

def aes_func(filePath, encFilePath, decFilePath):
    print(f"passed file path: {filePath}, encFilePath: {encFilePath}, decFilePath: {decFilePath}")
    key = Fernet.generate_key()
    f = Fernet(key)
    print("AES key: ", key)

    dirList = os.listdir(filePath)

    #remove hidden files from array that should not be encrypted
    dirList = rmdot.rm_dot(dirList, filePath)

    #creating start timestamp
    start = time.perf_counter()

    i = 0
    while i < len(dirList):
        #opening image and assigning bytes to token var
        with open(os.path.join(filePath, dirList[i]), 'rb') as originalFile:
            token = originalFile.read()

        encrypted = f.encrypt(token)

        #writing encrypted image file
        with open(os.path.join(encFilePath, dirList[i]), 'wb') as encryptedFile:
            encryptedFile.write(encrypted)
        print("Encrypted file ", i)
        i += 1

    middle = time.perf_counter()
    print("\nFinished encryption.\n")


