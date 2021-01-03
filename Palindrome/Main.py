#Function determinate if is palindrome a phrase
def is_Palindrome(sentence): 
    sentence = sentence.replace(' ','')
    sentence = sentence.lower();
    inverse_Sentence = sentence[::-1]
    if sentence == inverse_Sentence:
        return True
    else:
        return False

#Lets determinate if a word is a palindrome
def main():
    sentencePalindrome = input("Give me a sentence: ")
    if is_Palindrome(sentencePalindrome):
        print("Is palindrome")
    else:
        print("Is not a palindrome")

if __name__ == '__main__':
    main()