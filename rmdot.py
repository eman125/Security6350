import os

#remove hidden .files and directories from array of file names
def rm_dot(dirList, filePath):
    i = 0
    while i < len(dirList):
        path = os.path.join(filePath, dirList[i])
        if(os.path.isdir(path) or dirList[i][0] == "."):
            print("Removing: ", dirList[i], " from dirList")
            dirList.remove(dirList[i])
        else:
            i += 1

    return dirList

