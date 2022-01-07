#country = raw_input("Where do you live? ")
#print("You live in " + country)
import random
print("I'm thinking of a number between 1 and 10")
thought_number = random.randint(1,10)
number = input("What number am I thinking of?") #taking input into variable
number = int(number) #converting the number into integer
if number == thought_number:
    print("Thas Rite")
else:
    print("Nice try fella, the number was " + str(thought_number)) #converting int to string to add and print
