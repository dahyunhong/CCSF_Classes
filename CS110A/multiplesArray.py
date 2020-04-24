number = int(input('Choose number to start.'))
multiple = int(input('How many multiples?'))

multiples = []

for i in range(multiple):
    multiples.append(number*(i+1))
print(multiples)
