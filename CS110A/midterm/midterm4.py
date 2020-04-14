# Question 3

pay = 0.01
day = int(input("How many days did you work? "))
sum = 0
print("Day", "Pay", "Total", sep="  ")
for i in range(day):
    sum = round(sum+pay, 2)
    print(i+1, pay, sum, sep="   ")
    pay = round(pay*2, 2)
print("your next daily pay will be $", pay, sep="")
print("Total until now is $", sum, sep="")
