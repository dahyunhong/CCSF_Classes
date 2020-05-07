"""
Dahyun Hong
removeDuplicates.py
CS110A

"""


def removeDuplicates(list):
    """
    Removes duplicates from list

    Parameters:
      int[]: list: A list of numbers

    Returns:
      int[]: The number list with duplicates removed
    """
    newList = []
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList


def getList():
    """
    Get the list from the user, if the user enter the non positive integer or
    the letter q, the function will stop.

    Returns:
      int[]: The number list
    """
    again = 'y'
    list = []
    print("Please enter some positive integers, hitting return after each one. Enter 'q' to quit: ")

    while (again != 'q'):
        num = input('')
        if(num.isdigit() and int(num) > 0):
            list.append(num)
        else:
            again = 'q'

    return list


def large(list):
    """
    Returns the largest number in the list.

    Parameters:
      int[]: list: A list of numbers

    Returns:
      int: result: The largest number in the list
    """
    largest = list[0]
    for elem in list:
        if(elem > largest):
            largest = elem
    return largest


def small(list):
    """
     Returns the smallest number in the list.

     Parameters:
       int[]: list: A list of numbers

     Returns:
       int: result: The largest number in the list
     """
      smallest = list[0]
       for elem in list:
            if(elem < smallest):
                smallest = elem
        return smallest


def main():

    list = getList()  # [1, 2, 3, 4, 5, 5, 5, 6]
    noDup = removeDuplicates(list)  # [1,2,3,4,5,6]
    print("You entered {} unique number(s)".format(len(noDup)))  # 6
    print("with minimum value: {}, and maximum value: {}".format(
        small(noDup), large(noDup)))


main()
