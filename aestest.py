import time
import os
from cryptography.fernet import Fernet

def aes_func(filePath, encFilePath, decFilePath):
    print(f"passed file path: {filePath}, encFilePath: {encFilePath}, decFilePath: {decFilePath}")
    key = Fernet.generate_key()
    f = Fernet(key)
    print("AES key: ", key)

    dirList = os.listdir(filePath)
