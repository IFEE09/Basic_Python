def print_Name():
    print("Your correctly way to write your name is: " + name)
    return 0
    
name = input("What is your name: ")

name = name.capitalize() #The first with the UpperCase
name = name.strip() #This clean all the trash spaces
nameReplacedAO = name.replace('a','o') #this method replace all the a for 0
nameFirstLetter = name[0]
nameSecondLetter = name[1]
numberName = name.lenght()
numberName2 = len(name)

print_Name()
print("We replaced the a for o in your name " + nameReplacedAO)