import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        else:
            return False
    elif comp=='p':
        if you=='r':
            return False
        else:
            return False
    elif comp=='s':
        if you=='r':
            return True
        else:
            return False

print('computer\'s turn: rock(r) paper(p) or scissor(s)')
rando=random.randint(1,3)
if rando==1:
    comp="r"
elif rando==2:
    comp="p"
else:
    comp="s"

you=input('you turn:')
a=gamewin(comp,you)
print(comp)
if a==None:
    print('Tie')
elif a==True:
    print('you win')
else:
    print('you lose')