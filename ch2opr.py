a=30
b=40

#arithmetic

print('the value of 3+4 is ', 3+4)
print('the value of 3+4 is ', 3-4)
print('the value of 3+4 is ', 3*4)
print('the value of 3+4 is ', 3/4)

#assignment

a+=3
print(a)
a-=4
print(a)
a*=10
print(a)
a/=5
print(a)

#comparison

b=(14==7)
print(b)
b=(14<=7)
print(b)
b=(14>=7)
print(b)
b=(14<7)
print(b)
b=(14>7)
print(b)
b=(14!=7)
print(b)

#logical

a=True
b=False
print(a or b)
print(a and b)
print(not a)

#type casting

a="1234"
b=1234
print(a)
print(type(a))
print(int(a)+5)
print(type(int(a)))
print(str(b))
print(type(str(b)))
print(str(b)+'abc')
print(float(a))
print(float(b))

#input

a=input('enter your age ')
print(type(a))
a=int(a)
print(type(a))