a=[11,True,False,25.25,"repeat"]
print(a[0])
a[0]=101
print(a)

#slicing

friends=["hi","hello","how are you","how you doing"]
print(friends)
print(friends[0:3:2])

#list functions

l1=[1000,890,78,12,1722,712,771]
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(45)
print(l1)
l1.insert(0,555)
print(l1)
l1.pop(2)
print(l1)
l1.remove(555)
print(l1)