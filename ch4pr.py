t=(1,3,67)
print(t[2])


a=[]
a.append(input("enter fruit 1: "))
a.append(input("enter fruit 2: "))
a.append(input("enter fruit 3: "))
a.append(input("enter fruit 4: "))
a.append(input("enter fruit 5: "))
a.append(input("enter fruit 6: "))
a.append(input("enter fruit 7: "))
print(a)


b=[]
b.append(int(input("enter marks of student 1: ")))
b.append(int(input("enter marks of student 2: ")))
b.append(int(input("enter marks of student 3: ")))
b.append(int(input("enter marks of student 4: ")))
b.append(int(input("enter marks of student 5: ")))
b.append(int(input("enter marks of student 6: ")))
b.sort()
print(b)
print(sum(b))


c=(7,0,8,0,0,9)
print(c.count(0))