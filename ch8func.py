
def percent(marks):
    percentage=(sum(marks)/400)*100
    return percentage

marks1=[45,98,28,39]
print(percent(marks1))

marks2=[45,56,28,39]
print(percent(marks2))

marks3=[45,98,78,39]
print(percent(marks3))


def greet(name='stranger'): #declaring default
    print('have a good day, '+name)

greet('ginni')
greet()


def sum(n,m):
    return n+m

loda=int(input('enter first number '))
lasun=int(input('enter second number '))
s=sum(loda,lasun)
print(s)


def fact(n):
    if n==1 or n==0:
        return 1
    m=n*fact(n-1)
    return m

num=int(input('enter a number'))
print(fact(num))