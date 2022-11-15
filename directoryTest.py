import os

path = input("Please ender directory: ")
dirList = os.listdir(path)

i = 1
print("deleting second file which is: ", dirList[1])
dirList.remove(dirList[i])
print("dirList is now: ", dirList)
