import datetime
#from exit_convertime import *      #importing everything in exit.py     #exit_convertime
#from find_file import*             #find_file.py
import time
import os


#functions

def timeconverter():

    global time                                       #declare it as a global variable, if not local variable error
    a = input("press a to continue, x to exit: \n")

    if a == 'a':
        timestamp_bag = float(input("\nInsert the timestamp you wanna convert: "))
            
    
        #epoch_time = timestamp_bag
        
    
        date_time = datetime.datetime.fromtimestamp( timestamp_bag )  
        
    
        print("Given rosbag timestamp: ", timestamp_bag)  
        print("Converted Datetime: ", date_time )  
        

        time = date_time.time()

        hour = time.hour
        print("Hour : {}".format(hour))
        
        minute = time.minute
        print("Minute : {}".format(minute))


        print(hour)
        print(minute)
    

        #if (minute > 32):
        #    print("choose bagfile with 9:32 ")

        
        #keyword = input("what bag files you wanna find?\n")
        
        find_hr = str(hour)
        find_min = str(minute)
        for fname in os.listdir('/home/kitwei/Desktop/rosbag-project'):
            if find_hr and find_min in fname:
                print(fname, "has the keyword")


        

    elif a == 'x':
        print("exciting .......................")
        time.sleep(0.2)
        print("exciting  .....................")
        time.sleep(0.2)
        print("exciting   ...................")
        time.sleep(0.2)
        print("exciting    .................")
        time.sleep(0.2)
        print("exciting     ...............")
        time.sleep(0.2)
        print("exciting      .............")
        time.sleep(0.2)
        print("exciting       ...........")
        time.sleep(0.2)
        print("exciting        .........")
        time.sleep(0.2)
        print("exciting         .......")
        time.sleep(0.2)
        print("exciting          .....")
        time.sleep(0.2)
        print("exciting           ...")
        time.sleep(0.2)
        print("exciting            .")
        time.sleep(0.2)
     

    else:
        print("error")



#code starts here

choose_file = input("What file do you wanna use? \n")
#choose_file, keyword= input("What file do you wanna use? Enter the keyword you wanna find! \n").split()

full_dir = "/home/kitwei/Desktop/rosbag-project/" + choose_file


x = open(full_dir,"r")      #set it to a variable ######
 
keyword = input("Enter keyword: ")
#keyword = input("Enter keyword: ")



for line in x:                                   #search line by line
    if keyword in line:
        print(line)




timeconverter()



x.close()

print("")
print("")
print("end")







    