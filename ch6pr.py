
eng=int(input('enter english marks '))
math=int(input('enter maths marks '))
science=int(input('enter science marks '))
total=eng+math+science
if (total>=120) and (eng>=33) and (math>=33) and (science>=33):
    print('pass')
else:
    print('fail')


comment=input('please comment')
spam=['make a lot of money','buy now','subscribe this','click this']

if (spam[0] in comment) or (spam[1] in comment) or (spam[2] in comment) or (spam[3] in comment):
    print('spam detected')
else:
    print('comment ok')


username=input('enter a username')
if len(username)<10:
    print('less than 10')
else:
    print('ok')


name=input('enter name')
list=['harry','pooja','virat']
if name in list:
    print('present')
else:
    print('absent')


marks=int(input('enter marks'))
if marks<=100 and marks>90:
    print('Ex')
elif marks<=90 and marks>80:
    print('A')
elif marks<=80 and marks>70:
    print('B')
elif marks<=70 and marks>60:
    print('C')
elif marks<=60 and marks>50:
    print('D')
else:
    print('F')


a=['harry', 'HARRY','Harry',]
post=input('paste post here: ')
if (a[0] in post) or (a[1] in post) or (a[2] in post):
    print('talks about harry')
else:
    print('doesn\'t')