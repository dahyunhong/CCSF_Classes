# Write a program (convert_money.py) that prompts the user like this: “Currency to convert to U.S. dollars: e = Euros, c= Chinese Yuan, r = Indian Rupees, b = Bitcoin: ”. Then depending on which letter the user enters, the program displays “Amount of Euros/Yuan/Rupees/Bitcoin to convert: ”. (Note: the second prompt should only name the one currency the user asked to convert, not all four currencies.) After the user enters the amount, the program displays “In U.S. dollars, that is $N”, (N is the amount converted to U.S. dollars). (6 points)
# Conversion rates (from Google, Aug 6, 2018):


# 1 Euro =     1.16 US dollar
# 1 Chinese     yuan = 0.15 US dollar
# 1 Indian     rupee = 0.015 US dollar
# 1 Bitcoin     = 6923.80 US dollar
convert_money = (input(
    "Currency to convert to U.S. dollars: e = Euros, c= Chinese Yuan, r = Indian Rupees, b = Bitcoin: "))
dollars = 0
if(convert_money == 'e'):
    dollars = int(input("Amount of Euros:"))
    Euros = dollars * 1.16
    print("In U.S. dollars, that is ${}".format(Euros))

elif(convert_money == 'c'):
    dollars = int(input("Amount of Euros:"))
    chineseYuan = dollars * 0.15
    print("In U.S. dollars, that is ${}".format(chineseYuan))


elif(convert_money == 'r'):
    dollars = int(input("Amount of Euros:"))
    indianRupees = dollars * 0.015
    print("In U.S. dollars, that is ${}".format(indianRupees))

elif (convert_money == 'b'):
    dollars = int(input("Amount of Euros:"))
    Bitcoin = dollars * 6923.80
    print("In U.S. dollars, that is ${}".format(Bitcoin))
else:
    print("You didn't enter a valid option")
