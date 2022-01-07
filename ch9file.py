
f=open('sample.txt') #default mode is read
#data=f.read()
data=f.read(5) #reads first 5 char
print(data)
f.close()


f=open('sample.txt') #default mode is read
data=f.readline()#reads first line
print(data,end='')
data=f.readline()#reads second line
print(data)
f.close()


f=open('another.txt','w')
f.write('please 2 write this to the file\n')
f.close()


f=open('another.txt','a')
f.write('append\n')
f.close()


with open('sample.txt') as f:
    a=f.read()
    print(a)