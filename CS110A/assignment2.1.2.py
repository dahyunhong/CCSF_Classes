# 2.    Write a program to take the input of a number, and then check if it is a armstrong number or not.  An armstrong number is one in which sum of the cubes of the digits is equal to the number itself. You program should display an appropriate message.


# For example:

# 153 = 1^3 + 5^3 + 3^3

number = int(input('enter number: '))
digits = [int(x) for x in str(number)]
armstrong = 0

for i in range(len(digits)):
    armstrong += digits[i] ** 3


if armstrong == number:
    print("Its armstrong number")
else:
    print("Its not armstron number")
