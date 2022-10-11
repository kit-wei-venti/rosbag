import datetime
import time





def timeconverter():

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



        if (minute > 32):
            print("choose bagfile with 9:32 ")
        

    elif a == 'x':
        print("exciting.")
        time.sleep(0.2)
        print("exciting..")
        time.sleep(0.2)
        print("exciting...")
        time.sleep(0.2)
        print("exciting....")
        time.sleep(0.2)
        print("exciting.....")
        time.sleep(0.2)
        print("exciting......")
        time.sleep(0.2)
        print("exciting.......")
        time.sleep(0.2)
        print("exciting........")


    else:
        print("error")

    