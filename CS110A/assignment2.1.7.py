# Write a program to take the input of a number n and then find and display it’s factorial(n!). For example 4 != 1x2x3x4


number = int(input('Enter the number: '))
factorial = 1

for num in range(2, number+1):
    factorial *= num

print(factorial)
# 1*2*3*4*5

# 1*2(i)=2
# 2*i(3)=6
# 6*i(4)=24
# 24*5=120
# 120*6=720
# 720*7=490
