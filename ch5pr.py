h2e={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("options are ", h2e.keys())
a=input("enter hindi word\n")
print('the meaning of your word is:', h2e.get(a))

b=set()
b.add(int(input("enter number 1 ")))
b.add(int(input("enter number 2 ")))
b.add(int(input("enter number 3 ")))
b.add(int(input("enter number 4 ")))
b.add(int(input("enter number 5 ")))
b.add(int(input("enter number 6 ")))
b.add(int(input("enter number 7 ")))
b.add(int(input("enter number 8 ")))
print(b)


s=set()
s.add(20)
s.add(20.0) #equal hence wont add
s.add("20")
print(s)
print(len(s))


lang={}
lang.update({input("please enter your name: "):input("enter your fav lang: ")})
lang.update({input("please enter your name: "):input("enter your fav lang: ")})
lang.update({input("please enter your name: "):input("enter your fav lang: ")})
lang.update({input("please enter your name: "):input("enter your fav lang: ")})
print(lang)
