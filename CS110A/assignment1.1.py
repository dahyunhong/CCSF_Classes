# 1. Write a program to take the input of  number of seconds from the user, and  convert the number of seconds to hours, minutes, and seconds.

# For example, if seconds = 8000, then the output should be as follows:

# Hours=2

# Minutes=13

# Seconds=20

second = int(input("How many seconds? "))
hours = 0
minute = 0


while (second > 3600):
    hours += 1
    second -= 3600
6
while(second > 60):
    minute += 1
    second -= 60

print("hours = {}".format(hours))
print("minute = {}".format(minute))
print("second = {}".format(second))

# 2. Suppose you want to deposit a certain amount of money into a savings account and leave it alone to draw interest for the next 10 years. At the end of 10 years, you would like to have $10,000 in the account. How much do you need to deposit today to make that happen? Rate of interest is 2.99. You can use the following formula to find out:

p = round(10000/((1+0.0299)**10), 2)
print("you need to deposit ${}".format(p))
# The terms in the formula are as follows:

# P is the present value, or the amount that you need to deposit today.

# F is the future value that you want in the account. (In this case, F is $10,000.)

# r is the annual interest rate.

# n is the number of years that you plan to let the money sit in the account.
