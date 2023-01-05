import time
import os
import rmdot
import camellia

def camellia_func(filePath, encFilePath, decFilePath):
    print(f"passed file path: {filePath}, encFilePath: {encFilePath}, decFilePath: {decFilePath}")
    #defining key and initialization vector
    c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
    c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)

    dirList = os.listdir(filePath)

    #remove hidden files from array that should not be encrypted
    dirList = rmdot.rm_dot(dirList, filePath)

    #start timestamp
    start = time.perf_counter()

    i = 0
    while i < len(dirList):
