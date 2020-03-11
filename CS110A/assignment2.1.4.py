#  Write  a program to accept a number from the user and print its 10 multiples in the format shown in the sample output:

# Sample Output:

# Enter a number: 2

#                         2 X 1 = 2

#                         2 X 2 = 4

#                         :

#                         :

#                        2 X 10 = 20

number = int(input('Enter the number : '))

for i in range(1, 11):
    multiple = number * i
    print('{} x {} = {}'.format(number, i, multiple))
