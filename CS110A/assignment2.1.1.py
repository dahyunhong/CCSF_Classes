# 1.  Write a program to find the sum of the following series(up to N terms). The program should    display the terms:

#     22 + 42 + 62…

# For example, if N = 4, then the program should display the following terms:

#     4      16    36     64

# Sum of terms = 120

number = int(input('how many terms? '))
sum = 0
term = 2

for i in range(number):
    sum += term**2
    term += 2

print("Sum of terms: {}".format(sum))
