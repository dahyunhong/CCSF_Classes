def repeatChar(numRepeats, outputChar):
    '''
    output the outputChar numRepeats times
    '''
    for colNo in range(numRepeats):
        print(outputChar, end='')


def printParrallelogram(side, char):
    for i in range(side):
        repeatChar(i+1, char)
        print()
    for i in range(side):
        repeatChar(i+1, ' ')
        repeatChar(side-i-1, char)
        print()


def outlineParallelogram(side, char):
    for i in range(side):
        if (i < 1):
            repeatChar(1, char)
        elif(i == 1):
            repeatChar(2, char)
        else:
            repeatChar(1, char)
            repeatChar(i-1, ' ')
            repeatChar(1, char)
        print()
    for i in range(side-1):
        if (i == side-2):
            repeatChar(side-1, ' ')
            repeatChar(1, char)
        else:
            repeatChar(i+1, ' ')
            repeatChar(1, char)
            repeatChar(side-i-3, ' ')
            repeatChar(1, char)
        print()


print('This program will output a parallelogram')
number = int(input('How long do you want each side to be? '))
character = input('Enter the character: ')

printParrallelogram(number, character)
outlineParallelogram(number, character)

print()
