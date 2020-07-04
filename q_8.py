# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(num):
    if num>1:
        if (num==2):
            return True
        for i in range(2,num):
            if (num%i)==0:
                return False
            else:
                return True
    else:
        return False

def main():
    num = int(input("Enter any number."))
    is_prime(num)
    if True:
        print('Number is prime')
    else:
        print('Number is not prime')


if __name__ == "__main__":
    main()