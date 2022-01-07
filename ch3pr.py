you=input("Please neter your name\n")
print("good afternoon,\t", you)


letter='''Dear <|NAME|>
you are selected
date: <|DATE|>'''
name=input("please enter name: ")
date=input("please enter date: ")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)


example="string with double  spaces"
print(example)
doublespace=example.find("  ")
print(doublespace)


example=example.replace("  "," ")
print(example)

format="dear dikshant, this is nice. thanks!"
print(letter)
better="dear dikshant, \n\tthis is nice. \nthanks!"
print(better)