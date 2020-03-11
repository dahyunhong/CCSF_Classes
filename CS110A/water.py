# Write a program water.py that asks for temperature in Fahrenheit. The program should accept any floating point number. Display whether water is liquid, solid, or gas at that temperature at sea level. Display the results like this: “Water at that temperature is a solid/liquid/gas.” (Note: display only the correct state for that temperature.)
# Facts: At sea level, water freezes at 32 degrees F and boils at 212 degrees F. (4 points)

# Extra credit: 1 point if you convert the temperatures to celsius when printing.


temp = float(input("How many degrees in fahrenheit?"))
if(temp < 32):
    print("water temperture is solid")  # ice
elif(temp > 32 and temp < 212):
    print("water temperture is liquid")  # water
else:
    print("water temperture is gas")
