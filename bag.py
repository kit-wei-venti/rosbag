x = open('2022年09月13日星期二09293708.txt','r')      #set it to a variable
 
keyword = input("Enter keyword:")

for line in x:                                   #search line by line
    if keyword in line:
        print(line)

x.close()


