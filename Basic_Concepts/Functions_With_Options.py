def greeting():
    print("Hi, how are you?")
    print("Nice you selected the " , option , " option")
    print("Good bye!")

option = int(input("Select 1, 2 or 3 please: "))

if option == 1:
    greeting()
elif option == 2:
    greeting()
elif option == 3:
    greeting()
else:
    print("Invalid option, restart and try again")