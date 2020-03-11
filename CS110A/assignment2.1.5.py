# 5. Write  a program to take the input of a number and then find and display  the following(Hint: Use modules operator to extract the digits):

# a. sum of even digits

# b. sum of odd digits

# c. total number of even digits

# d. total number of odd digits


# For example, if number = 3421, then  your output should be

# Sum of even digits = 6 4+2

# Sum of odd digits = 4 3+1

# Number of even digits = 2 2,4

# Number of odd digits = 2 1,3

number = int(input('enter number: '))
digits = [int(letter) for letter in str(number)]
even = 0  # how many evens
odd = 0
sumOdd = 0
sumEven = 0

for num in digits:
    if num % 2 == 0:
        even += 1
        sumEven += num
    else:
        odd += 1
        sumOdd += num

print('sum of even is {}'.format(sumEven))
print('Sum of odd digits is {}'.format(sumOdd))
print('Number of even digits {}'.format(even))
print('Number of odd digits is {}'.format(odd))
