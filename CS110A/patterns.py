

n = int(input('Enter the number : '))
# A
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()


# B
print()
pattern = ""

for i in range(n):
    for j in range(i+1):
        pattern = str(j+1) + pattern
    print(pattern)
    pattern = ""


#  a = "1"
#  print
#  b = "21"
#  c = "321"
#  d = "4321"

# C
# 1234
# 123
# 12
# 1
print()
patterns = []
pattern = ""


for i in range(n):
    for j in range(i+1):
        pattern = pattern + str(j+1)
    patterns.insert(0, pattern)
    pattern = ""

for num in patterns:
    print(num)

# 4321
# 321
# 21
# 1
print()
patterns = []
pattern = ""


for i in range(n):
    for j in range(i+1):
        pattern = str(j+1) + pattern
    patterns.insert(0, pattern)
    pattern = ""

for num in patterns:
    print(num)
