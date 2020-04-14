def even_or_odd(n):
    if n % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')


def main():
    number = int(input("Enter the number: "))
    even_or_odd(number)


main()
