setting_file = open("User.txt", "r")
name = setting_file.readline()
setting_file.close()
if name == "":
    name_input = input("Please enter name: ")
    setting_file = open("User.txt", "w")
    setting_file.write(name_input)
    setting_file.close()
    print("Thanks, " + name_input)
else:
    print("Nice to have you back, " + name)
    emotion = input("How do you feel? ")
    if "good" in emotion:
        print("Great, have a good day")
    elif emotion.find("not") != -1:
        print("Better luck next time")
    else:
        print("I don't get you")
