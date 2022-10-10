# importing the datetime package  
import datetime  
  





#read data from a text file
with open('2022年09月13日星期二09293708.txt') as fo:  #if u wanna read then r , eg if u wanna write then w #open func to open the file
    for rec in fo:
        print(rec[0:5])




#read = file.readlines()                             #reading line by line
#modified = []


'''for line in read:

    modified.append(line.strip())


    if line[-1] == '\n':                           
        modified.append(line[:-1])                  #remove the \n


    else:
        modified.append(line) '''



















#code use to convert timestamp from rosbag to earth time
# given epoch time  
epoch_time = 40246871  
  
# using the datetime.fromtimestamp() function  
date_time = datetime.datetime.fromtimestamp( epoch_time )  
  
# printing the value  
print("Given epoch time:", epoch_time)  
print("Converted Datetime:", date_time )  