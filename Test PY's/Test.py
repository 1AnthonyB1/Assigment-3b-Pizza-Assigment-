#Calculations for Size to Price
def main():
    Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))
    Flag = 0
    Flag2 = 0
    Price = 0

#Large Recignition & Price Calculation
    CapsSize = str.upper(Size)
    if CapsSize == "LARGE":
        Price = Price + 6.00
    elif CapsSize == "L":
        Price = Price + 6.00

#Extra large Recignition & Price Calculation
    elif CapsSize == "EXTRA LARGE":
        Price = Price + 10.00
    elif CapsSize == "XL":
        Price = Price + 10.00

#Size Flag Check
    if CapsSize == "EXTRA LARGE":
        Flag = Flag + 1
    elif CapsSize == "XL":
        Flag = Flag + 1
    elif CapsSize == "L":
        Flag = Flag + 1
    elif CapsSize == "LARGE":
        Flag = Flag + 1

#Size Valid Imput Check
    if Flag == 0:
        print()
        print("Invalid Imput")

    if Flag == 0:
        main()
main()

#Calculation for Number's of toppings to Price
def main2():

    Toppings = (input("\nWhat Number of toppings do you want: \n1,2,3 or 4? \nType Number of Toppings:"))
    ToppingsSize = str.upper(Toppings)

#Variations of 1
    CapsToppings = str.upper(Toppings)
    if Toppings == "1":
        Price = Price + 1.00
    elif CapsToppings == "ONE":
        Price = Price + 1.00

#Variations of 2
    elif Toppings == "2":
        Price = Price + 1.75
    elif CapsToppings == "TWO":
        Price = Price + 1.75

#Variations of 3
    elif Toppings == "3":
        Price = Price + 2.50
    elif CapsToppings == "THREE":
        Price = Price + 2.50

#Variations of 3
    elif Toppings == "4":
        Price = Price + 3.35
    elif CapsToppings == "FOUR":
        Price = Price + 3.35

#Toppings Flag Check
    if ToppingsSize == "ONE":
        Flag2 = Flag2 + 1
    elif ToppingsSize == "TWO":
        Flag2 = Flag2 + 1
    elif ToppingsSize == "THREE":
        Flag2 = Flag2 + 1
    elif ToppingsSize == "FOUR":
        Flag2 = Flag2 + 1
    elif Toppings == "1":
        Flag2 = Flag2 + 1
    elif Toppings == "2":
        Flag2 = Flag2 + 1
    elif Toppings == "3":
        Flag2 = Flag2 + 1
    elif Toppings == "4":
        Flag2 = Flag2 + 1
#Size Valid Imput Check
    if Flag2 == 0:
        print()
        print("Invalid Imput")

    if Flag2 == 0:
        main2()
main2()

#Calculation Pizza Price into Pizza Price + Tax
TaxPrice = (float(Price)*0.13)
FinalPrice = (TaxPrice + Price)

print()
print("This is your Subtotal: $",FinalPrice - TaxPrice)
print("This is your Tax: $",TaxPrice)
print("This is your Final Price: $", FinalPrice)