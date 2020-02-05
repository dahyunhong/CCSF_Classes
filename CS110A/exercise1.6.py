rad = float(input("Enter the radius:"))

Area=3.14*rad*rad

Circumference=2*3.14*rad

print("The area is {}".format(Area))
print("The circumference is {}".format(Circumference))


# 2.  Write a program to take the input of two numbers and then swap their values. Your code should display the original and the modified  values of the variables .

# For example:

# Enter First variable: 5

# Enter Second variable: 10

# Original First=5

# Original Second=10

# New First=10

# New Second=5

first = input("Enter First variable: ")
second = input("Enter Second variable: ")
print("Original First is {}" .format(first))
print("Original Second is {}" .format(second))
temp = first
first = second 
second = temp

print("New First is {}" .format(first))
print("New Second is {}" .format(second))


# 3.  Write  a program in python to  convert temperature from Celsius to Fahrenheit.

Celsius = float(input("input Celsius; "))
F = (Celsius * (9/5)) +32
print("Fahrenheit is {}" .format(F))
# (0°C × 9/5) + 32 = 32°F

F = float(input("input Fahrenheit; "))
Celsius = (F-32) *(5/9)
print("celsius is {}" .format(Celsius))
# (32°F − 32) × 5/9 = 0°C


