import os

filePath = input("Please enter file path: ")

with open(filePath, 'rb') as originalFile:
    token = originalFile.read()

print(type(token))
print("token: ", token)
