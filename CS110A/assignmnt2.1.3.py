# 3.  Write a program to accept a number and then check whether it is a prime number or a composite number. Your program should display an appropriate message. A prime number is one which is divisible by itself and 1Sample Outputs:

# Enter a number: 5

# It is a prime number.

# Enter a number: 12

# It is a composite number.

number = int(input('Enter the number: '))
prime = True
for i in range(2, int(number/2)):
    if (number % i == 0):
        prime = False

if prime == True:
    print('It is a prime number')
else:
    print('It is a composite number')
