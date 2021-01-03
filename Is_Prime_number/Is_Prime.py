def is_Prime(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter > 2:
        return False
    else:
        return True

def main():
    number = int(input("Give me a number please: "))
    if is_Prime(number):
        print("The number is prime ")
    else:
        print("The number is not prime ")

if __name__ == "__main__":
    main()
