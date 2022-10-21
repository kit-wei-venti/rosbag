import datetime
import time
import os




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

        


        when = date_time.date()

        year = when.year
        print("Year : {}".format(year))

        month = when.month
        print("Month : {}".format(month))

        day = when.day
        print("Day : {}".format(day))


        print(hour)
        print(minute)
        
    

        #if (minute > 32):
        #    print("choose bagfile with 9:32 ")

        
        #keyword = input("what bag files you wanna find?\n")
        
        find_hr = str(hour)
        find_year = str(year)
        find_month = str(month)
        find_day  = str(day)
        

        for fname in os.listdir('/home/kitwei/Desktop/rosbag-project'):
            if '.bag' and find_year and find_month and find_day in fname:
                print(fname)
                #print(fname, "has the keyword")


        

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





timeconverter()