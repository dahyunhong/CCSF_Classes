def even_or_odd():
    number = int(input('Enter the number: '))
    even = number % 2
    if even == 0:
        print("This is an even number")
    else:
        print("This is an odd number")


def main():
    even_or_odd()


main()
