x = open('random.txt','r')

for line in x:
    if 'hello' in line:
        print(line)

x.close()