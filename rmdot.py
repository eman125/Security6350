#remove hidden files (.files) from array of file names
def rm_dot(dirList):
    i = 0
    while i < len(dirList):
        if(dirList[i][0] == "."):
            print("Removing file: ", dirList[i], " from dirList")
            dirList.remove(dirList[i])
            i += 1
        else:
            i += 1

    return dirList
