def main():
    for counter in range(1,101):
        if counter % 2 != 0:
            continue #this pass the condition and continue with the numbers who complete the condition
        print(counter)
    
    for i in range(1, 101):
        print(i)
        if i == 21:
            break #this stop the for

    text = input("Give me a text: ") #This is for strings
    for letter in text:
        if letter == 'o':
            break
        print(letter)

if __name__ == '__main__':
    main()