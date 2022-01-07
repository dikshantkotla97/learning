
i=0
while i<10:
    print('yes ' + str(i))
    i=i+1
print('done')


fruits=['banana', 'apple', 'melon','grapes','mango']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1


fruits=['banana', 'apple', 'melon','grapes','mango']
for loda in fruits:
    print(loda)



for i in range(1,8,2):
    print(i)
    if i==5:
        break
else: #executed only on successful completion of for loop
    print('loda lasun')


for i in range(1,8):
    if i==5:
        continue #skips the sequence if encountered
    print(i)


i=4
if i>0:
    pass
while i>6:
    pass
print('lasun')
