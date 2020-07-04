# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def convert(word):
    snake_case = [word[0].lower()]
    kebab_case = [word[0].lower()]
    for letter in word[1:]:
        if letter == letter.upper():
            snake_case.append("_")
            kebab_case.append("-")
            snake_case.append(letter.lower())
            kebab_case.append(letter.lower())
        else:
            snake_case.append(letter)
            kebab_case.append(letter)
    
    print(''.join(snake_case))
    print(''.join(kebab_case))

def main():
    word = input("Enter camel-cased string")
    convert(word)


if __name__ == '__main__':
    main()
