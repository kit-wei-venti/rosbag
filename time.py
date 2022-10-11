# importing the datetime package  
import datetime  
  



#code use to convert timestamp from rosbag to earth time
# given epoch time  
epoch_time = 1663032661.474768992
  
# using the datetime.fromtimestamp() function  
date_time = datetime.datetime.fromtimestamp( epoch_time )  
  
# printing the value  
print("Given epoch time:", epoch_time)  
print("Converted Datetime:", date_time )  