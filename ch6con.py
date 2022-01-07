a=2
if(a>3):
    print("value greater than 3")
elif(a>7):
    print("value greater than 7")
elif(a>11):
    print("value greater than 11")
elif(a>15):
    print("value greater than 15")
else:
    print('not greater than 3')


b=None
if (b is None): #pointing to the same value, different from ==
    print('yes')
else:
    print('no')


c=[23,12,34,9,76]
print(23 in c)

