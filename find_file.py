import os             #use when dealing with file/directory


def find_file():


    search_bag_file = input("Name of text file? \n")

    rootDir = "/home/kitwei/Desktop"
    fileToSearch = search_bag_file

    for relPath, dirs, files in os.walk(rootDir):
        if fileToSearch in files:
            fullPath = os.path.join(rootDir, relPath,fileToSearch)
            print(fullPath)















