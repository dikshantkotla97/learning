'''
with open('practice.txt','w') as f:
    f.write('Twinle twinke little star')
with open('practice.txt','r') as f:
    a=f.read()
    print(a)
t=open('practice.txt')
g=t.read()
if 'twinkle' in g:
    print('present')
else:
    print('not present')
t.close()

'''

def game():
    return 640

score=game()
with open('highscore.txt') as h:
    highscore=int(h.read())

if highscore<score:
    with open('highscore.txt', 'w') as h:
        h.write(str(score))
