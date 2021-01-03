#we need to print al the 2 pow numbers from 1 to 10
def main():
    LIMIT = 10
    counter = 0
    two_Power = 2**counter
    while counter < LIMIT:
        counter += 1
        two_Power = 2**counter
        print(two_Power)

if __name__ == '__main__':
    main()
