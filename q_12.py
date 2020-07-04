# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):
    if (word==word[::-1]):
        print("The word is palindrame")
    else:
        print("The word is not palindrome")
    

def main():
    word = input("Enter word ")
    is_palindrome(word)

if __name__ == "__main__":
    main()