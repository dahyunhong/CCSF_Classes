# Write a program classify_age.py that asks the user to enter a person’s age. Then the program should display text indicating whether the person is an infant, a toddler, a child, a teenager, an adult, or a senior. It should display it just like this: “This person’s age category: x”, where x is
# the person’s age category based on the following guidelines (4 points):

# If less than 1 year old, the person is an infant.

# If at least 1 year old but younger than 3, the person is a toddler.

# If at least 3 years old but younger than 13, the person is a child.

# If at least 13 years old but younger than 18, the person is a teenager.

# If at least 18 years old but younger than 65, the person is an adult.

# If 65 or older, the person is a senior.
age = int(input("Enter the age:"))
if (age < 1):
    print("This person’s age category: infant")
elif(age >= 1 and age < 3):
    print("This person’s age category: toddler")
elif(age >= 3 and age < 13):
    print("This person’s age category: child")
elif(age >= 13 and age < 18):
    print("This person’s age category: teenager")
elif(age >= 18 and age < 65):
    print("This person’s age category: adult")
else:
    print("This person’s age category: senior")
