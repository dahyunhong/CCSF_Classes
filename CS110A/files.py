
def copy():
    pass


def main():
    choice = 1
    while choice != 6:
        print("1.  Copy a Text File")
        print("2.  Read number of lines of Text File")
        print("3.  Display Text File")
        print("4.  Display first five lines of Text File")
        print("5.  Run the Golf Club Program")
        print("6.  Exit.")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            copy()
        elif choice == 2:
            number_lines()
        elif choice == 3:
            display()
        elif choice == 4:
            first_five()
        elif choice == 5:
            golf_club()


main()
