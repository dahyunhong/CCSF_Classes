#  To take the input of a number and then check whether it is a palindrome number or not.  Find the reverse of  a number using a loop and then compare it with the original number. A palindrome number is a number which is same when read from front or end. For example, 1221 is a palindrome number.

number = int(input('enter number: '))
digits = [int(letter) for letter in str(number)]
reverse = []
for num in digits:
    reverse.insert(0, num)
# print(digits)
# print(reverse)
if digits == reverse:
    print('it is a palindrome number')
else:
    print('it is not a palindrome number')
