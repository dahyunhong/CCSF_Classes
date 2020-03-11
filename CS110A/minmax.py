number = int(input('please enter number:'))
minimum = number
maximum = number
while number != -1:
    if number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number
    number = int(input('please enter number:'))

print("The Minumum value{}".format(minimum))
print("The Maximum value{}".format(maximum))
