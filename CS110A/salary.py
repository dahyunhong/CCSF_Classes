def constant_salary():
    sum = 0
    for i in range(10):
        sum += 100
    return sum


def doubling_salary():
    sum = 0
    pay = 1
    for i in range(10):
        sum += pay
        pay *= 2
    return sum


def main():
    if constant_salary() < doubling_salary():
        print("doubling salary is better")
    elif constant_salary() == doubling_salary():
        print('They are the same.')
    else:
        print('constant salary is better')


main()
