import random
def run():
    counter_Of_Attempts = 5
    aleat = random.randint(1, 100)
    choose_Of_User = input('Guess a number:')

    while (choose_Of_User != aleat):
        if counter_Of_Attempts == 0:
            break
        print("Sorry, is not the number i think, try again you have ", counter_Of_Attempts , " attempts more")
        counter_Of_Attempts -= 1
        choose_Of_User = input('Guess a number:')

    print("the number i thinked was ", aleat)
    print("Good luck for the next time, good bye!")

if __name__ == '__main__':
    run()