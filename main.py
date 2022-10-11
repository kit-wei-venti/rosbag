import datetime
from exit_convertime import *      #importing everything in exit.py     #exit_convertime
#from find_file import*             #find_file.py




choose_file = input("What file do you wanna use? \n")

full_dir = "/home/kitwei/Desktop/rosbag-project/" + choose_file


x = open(full_dir,"r")      #set it to a variable ######
 
keyword = input("Enter keyword: ")

for line in x:                                   #search line by line
    if keyword in line:
        print(line)



timeconverter()


x.close()

print("")
print("")
print("end")



