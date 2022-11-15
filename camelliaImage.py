import time
import os
import camellia

filesPath = input("Please enter directory of desired files: ")
dirList = os.listdir(filesPath) #makes string array of all file names in directory
encFilePath = "/Users/emmanuelhuitron/Desktop/Encrypted"
decFilePath = "/Users/emmanuelhuitron/Desktop/Decrypted"

#removing hidden files from array that should not be encrypted
i = 0
while i < len(dirList):
    if(dirList[i][0] == "."):
        print("removing file: ", dirList[i], " from dirList")
        dirList.remove(dirList[i])
        i += 1
    else:
        i += 1

#defining key and initialization vector
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)

#starting timer
start = time.perf_counter()

i = 0
while i < len(dirList):
    #opening image and assigning bytes to the var "token"
    with open(filesPath + "/" + dirList[i], 'rb') as originalFile:
        token = originalFile.read()

    encrypted = c1.encrypt(token)

    #writing the encrypted image file
    with open(encFilePath + "/" + dirList[i], 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
    print("Encrypted file ", i)
    i += 1

middle = time.perf_counter()
print("Finished the encryption.")

dirList = os.listdir(encFilePath)
#removing hidden files from new dirList
i = 0
while i < len(dirList):
    if(dirList[i][0] == "."):
        print("removing file: ", dirList[i], " from dirList")
        dirList.remove(dirList[i])
        i += 1
    else:
        i += 1

#beginning decryption timestamp
startDec = time.perf_counter()

i = 0
while i < len(dirList):
    #opening encrypted image
    with open(encFilePath + "/" + dirList[i], 'rb') as encryptedFile:
        encrypted = encryptedFile.read()

    decrypted = c2.decrypt(encrypted)

    with open(decFilePath + "/" + dirList[i], 'wb') as decryptedFile:
        decryptedFile.write(decrypted)
    print("Decrypted file ", i)
    i += 1

finish = time.perf_counter()
print(f'***Finished encryption in {round(middle-start, 2)} second(s)***')
print(f'***Finished decryption in {round(finish-startDec, 2)} second(s)***')
print(f'***Finished overall in {round((middle-start) + (finish-startDec), 2)} second(s)***')
