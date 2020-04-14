
def add(number1, number2):
    result = number1 + number2
    print(result)


def subtract(number1, number2):
    result = number1-number2
    print(result)


def multiply(number1, number2):
    result = number1 * number2
    print(result)


def divide(number1, number2):
    result = number1/number2
    print(result)


def main():
    goAgain = 'y'

    while goAgain == 'Y' or goAgain == 'y':
        print("Welcome to the Calculator Program!")
        number1 = int(input("Enter the number: "))
        number2 = int(input("Enter the number: "))

        operation = input("Enter the mathematical operation.")

        operations = ['+', '-', '/', '*']

        while (operation not in operations):
            print("This is not a vaild operation symbol.")
            operation = input("Enter the mathematical operation.")
        if operation == '+':
            add(number1, number2)
        elif operation == '-':
            subtract(number1, number2)
        elif operation == '*':
            multiply(number1, number2)
        else:
            divide(number1, number2)
        goAgain = input('Do you want to go again? ')


main()
