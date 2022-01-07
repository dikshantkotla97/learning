
def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

print(max(int(input('1st num')),int(input('2nd num')),int(input('3rd num'))))



def farh(cel):
    return (cel*9/5+32)

print(farh(int(input('enter temp\n'))))



print('hello', end='') #by default end='\n',if end='', then no new line will be made
print('how', end='')
print('are', end='')
print('you?', end='')



def recursion(n):
    if n==1:
        return 1
    sum=n+recursion(n-1)
    return sum
print(recursion(int(input('enter a number'))))



def star(n):
    if n==1:
        return print('*')
    else:    
        print('*'*n)
    star(n-1)
star(int(input('enter number')))


def cms(inches):
    return (inches/2.54)

print(cms(int(input('enter inches\n'))))



def remove_and_split(string,word):
    newstr=string.replace(word, '')
    return newstr.strip()

string=input('enter string\n')
print(string)
word=input('word you want to remove\n')
print(remove_and_split(string,word))



def mult(num):
    for i in range(1,num+1):
        print(f'{num}X{i}={num*i}')

num=int(input('please enter a number: '))
mult(num)
