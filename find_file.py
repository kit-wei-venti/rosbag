import os             #use when dealing with file/directory



#try to display nearest timing file first



#anynumber = 34


'''def find_file():


    search_bag_file = input("Name of text file? \n")

    if search_bag_file > 32:
        rootDir = "/home/kitwei/Desktop"
        fileToSearch = search_bag_file

        for relPath, dirs, files in os.walk(rootDir):
            if fileToSearch in files:
                fullPath = os.path.join(rootDir, relPath,fileToSearch)
                print(fullPath)


    else :
        rootDir = "/home/kitwei/Desktop"
        fileToSearch = search_bag_file

        for relPath, dirs, files in os.walk(rootDir):
            if fileToSearch in files:
                fullPath = os.path.join(rootDir, relPath,fileToSearch)
                print(fullPath) '''


#find_file()





'''search_bag_file = input("Name of text file? \n")

if search_bag_file > 32:
    rootDir = "/home/kitwei/Desktop"
    fileToSearch = search_bag_file

    for relPath, dirs, files in os.walk(rootDir):
        if fileToSearch in files:
            fullPath = os.path.join(rootDir, relPath,fileToSearch)
            print(fullPath) '''



#code below is used to search for file based on file name

keyword = input("what bag files you wanna find?\n")
#keyword = '.bag'
for fname in os.listdir('/home/kitwei/Desktop/rosbag-project'):
    if keyword in fname:
        print(fname, "has the keyword")








