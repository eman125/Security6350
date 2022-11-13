import os

path = "/Users/emmanuelhuitron/Desktop"
dirList = os.listdir(path)

print("Files and directories in ", path, ": ")
print(dirList)
print("second item in list is: ", dirList[1])
