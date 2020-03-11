# Welcome to the CS 110 Pokemon Go Shop!

# Which Pokemon would you like to collect?

# 1. Bulbasaur

# 2. Pidgey

# 3. Butterfree

# 4. Sandslash

# 5. Exit Please enter your choice (1-5):
menu = """Welcome to the CS 110 Pokemon Go Shop!

Which Pokemon would you like to collect?

1. Bulbasaur

2. Pidgey

3. Butterfree

4. Sandslash

5. Exit Please enter your choice (1-5): """

Bulbasaur = 0
Pidgey = 0
Butterfree = 0
Sandslash = 0

response = int(input(menu))

while response != 5:
  if response < 1 or response > 4:
    print("Invalid choice \n")
    response = int(input(menu))
  else:
    #something else 
    if response == 1:
      Bulbasaur += int(input("How many Bulbasaur do you want to collect? "))
    elif response == 2:
      Pidgey += int(input("How many Pidgey do you want to collect? "))
    elif response == 3:
      Butterfree += int(input("How many Butterfree do you want to collect? "))
    else:
      Sandslash += int(input("How many Sandslash do you want to collect? "))
    print("")
    response = int(input(menu))

print("You collected: ")
print("Bulbasaur: {}".format(Bulbasaur))
print("Pidgey: {}".format(Pidgey))