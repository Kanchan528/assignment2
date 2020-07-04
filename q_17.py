# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

num1 = int(input("Enter the first number "))
operator = input("Enter any operator ")
num2 = int(input("Enter the second number "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("You can't divide by zero")



