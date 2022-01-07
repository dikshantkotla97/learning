number = 8
if number < 5:
    print ('Number is less than 5')
else:
    print('Number is greater than 5')


cities = ['newyork', 'washington', 'los angeles', 'san francisco', 'chicago']
number = len(cities)
number = number - 1
round = 0
while round <= number:
    print(cities[round])
    round = round + 1
print('End of the loop')
