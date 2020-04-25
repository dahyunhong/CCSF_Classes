NUM_LIST = 6
list = []


def large(list):
    largest = list[0]
    for elem in list:
        if(elem > largest):
            largest = elem
    return largest


def small(list):
    smallest = list[0]
    for elem in list:
        if(elem < smallest):
            smallest = elem
    return smallest


for i in range(NUM_LIST):
    list.append(int(input('Enter a number: ')))

print(list)
print("largest number is {}".format(large(list)))
print("smallest number is {}".format(small(list)))
