def main():
    num = int(input('Enter a number : '))
    print()
    displayNumbers(num)
    print()
    reverse(num)
    print()
    pattern(num)


def displayNumbers(n):
    for i in range(n):
        print(i+1)


def reverse(n):
    for i in range(n, 0, -1):
        print(i)


def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("$", end="")
        print()


main()
