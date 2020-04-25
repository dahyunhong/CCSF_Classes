NUM_LIST = 4
list = []


def large(list):
    largest = list[0]
    for elem in list:
        if(elem > largest):
            largest = elem
    return largest


def swapLarge(list):  # list = [3, 5, 6, 2]

    newList = []

    for elem in list:
        newList.append(elem)  # newList = [3, 5, 6, 2]
    print("new list is {}".format(newList))
    original_first = list[0]  # og_f = 3
    largestIndex = 0
    largest = large(list)

    for i in range(len(list)):
        if list[i] == largest:
            largestIndex = i

    print("largest index is {}".format(largestIndex))
    newList[0] = largest  # newlist = [6, 5, 6, 2]
    newList[largestIndex] = original_first  # newlist = [6, 5, 3, 2]

    return newList


for i in range(NUM_LIST):
    list.append(int(input('Enter a number: ')))

print("list is {}".format(list))
swapList = swapLarge(list)

print("original list is {}".format(list))  # [3, 5, 2, 6]
print("swapped list is {}".format(swapList))  # [6, 5, 2, 3]
