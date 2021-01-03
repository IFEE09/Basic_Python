import random
def password_generator():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lower = ['a', 'b', 'c', 'd', 'e', 'f']
    symbols = ['!', '#', '$', '&', '/', ')',]
    numbers = ['1', '2', '3', '4', '5', '6']

    characters_password = upper + lower + symbols + numbers

    password = []

    for i in range(15):
        characters_random = random.choice(characters_password)
        password.append(characters_random)
    
    password = "".join(password)
    return password

def main():
    setup = """
    Hi, this is a strong password generator
    -Press 1 to generate a new strong password
    -press 2 to exit
    """
    option = int(input(setup))

    if option == 1:
        password = password_generator()
        print("You new password is: " + password)
    elif option == 2:
        print("Nice to see you again, see you later!")
    else: 
        print("Invalid option, restart and try again")
    

if __name__ == '__main__':
    main()

