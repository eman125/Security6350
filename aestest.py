import time
import os
from cryptography.fernet import Fernet

def aes_func(filePath, encFilePath):
    print(f"passed file path: {filePath}")
    key = Fernet.generate_key()
    f = Fernet(key)
    print("AES key: ", key)

    dirList = os.listdir(filesPath)
