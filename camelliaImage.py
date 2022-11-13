import time
import os
import camellia

filesPath = input("Please enter directory of desired files: ")
dirList = os.listdir(filesPath) #makes string array of all file names in directory
encFilePath = "/Users/emmanuelhuitron/Desktop/Encrypted"
decFilePath = "/Users/emmanuelhuitron/Desktop/Decrypted"

#defining key and initialization vector
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)

#starting timer
start = time.perf_counter()

#opening image and assigning bytes to the var "token"
with open(filesPath + "/" + dirList[0], 'rb') as originalFile:
    token = originalFile.read()

encrypted = c1.encrypt(token)

#writing the encrypted image file
with open(encFilePath + "/" + dirList[0], 'wb') as encryptedFile:
    encryptedFile.write(encrypted)
print("Encrypted the file.")

middle = time.perf_counter()

#opening encrypted image
with open(encFilePath + "/" + dirList[0], 'rb') as encryptedFile:
    encrypted = encryptedFile.read()

decrypted = c2.decrypt(encrypted)

with open(decFilePath + "/" + dirList[0], 'wb') as decryptedFile:
    decryptedFile.write(decrypted)
print("Decrypted the file.")

finish = time.perf_counter()
print(f'***Finished encryption in {round(middle-start, 2)} second(s)***')
print(f'***Finished decryption in {round(finish-middle, 2)} second(s)***')
print(f'***Finished overall in {round(finish-start, 2)} second(s)***')
