#remove hidden files (.files) from array of file names
def rm_dot(dirList):
    i = 0
    while i < len(dirList):
        if(dirList[i][0] == "." or os.path.isdir(dirList[i])):
            print("Removing: ", dirList[i], " from dirList")
            dirList.remove(dirList[i])
            i += 1
        else:
            i += 1

    return dirList
