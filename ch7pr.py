
number=int(input('enter a number: '))
for i in range(1,11):
   # print(str(number) + 'X' + str(i) + '=' + str(i*number))
    print(f"{number}X{i}={number*i}") #f-string


l1=['harry','soham','sachin','rahul']
for name in l1:
    if name.startswith('s'):
        print('hello '+name)


i=1
num=int(input('enter number '))
while i<11:
    print(f'{num}X{i}={num*i}')
    i=i+1


num=int(input('enter the number\n'))
for i in range(2,num):
    if(num%i==0):
        print('not prime')
        break
else:
    print('prime')


n=int(input('enter a number\n'))
s=0
for i in range(1,n+1):
    s=s+i
print('sum of first '+str(n)+' natural numbers is '+str(s))


n=int(input('enter a number\n'))
for i in range(n-1,1,-1):
    n=n*i
print(n)


for i in range(1,6):
    print('*'*i)



n=int(input('enter number'))
for i in range(n):
    print(' '*(n-i-1),end='')
    print('*'*(2*i+1),end='')
    print(' ')


n=int(input('enter box size: '))
for i in range(n):
    if (i==0) or (i==n-1):
        print('* '*n)
    else:
        print('* ',end='')
        print('  '*(n-2),end='')
        print('*')


n=int(input('enter a number\n'))
for i in range(10,0,-1):
    print(f'{n} X {i} = {n*i}')