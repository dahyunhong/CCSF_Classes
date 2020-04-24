NUM_LIST = 6
list = []


def double(list):
    doubledList = []
    for i in list:
        doubledList.append(i*2)
    return doubledList


for i in range(NUM_LIST):
    list.append(int(input('Enter a number: ')))

print(list)
print(double(list))
