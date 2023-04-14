#Calculations for Size to Price
def main():
    Flag = 0
    Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))
    price = float(0)

#Large Recignition & Price Calculation
    CapsSize = str.upper(Size)
    if CapsSize == "LARGE" or CapsSize == "L":
        price = float(6.00)
        Flag = Flag + 1

#Extra large Recignition & Price Calculation
    elif CapsSize == "EXTRA LARGE" or CapsSize == "XL":
        price = float(10.00)
        Flag = Flag + 1

#Size Valid Imput Check
    if Flag == 0:
        print()
        print("Invalid Imput")

    if Flag == 0:
        main()
main()

#Calculation for Number's of toppings to Price
Toppings = (input("\nWhat Number of toppings do you want: \n1,2,3 or 4? \nType Number of Toppings:"))
ToppingsSize = str.upper(Toppings)
Flag2 = 0

#Variations of 1
CapsToppings = str.upper(Toppings)
if Toppings == "1":
    price = price + 1.00
    Flag2 = Flag2 + 1
elif CapsToppings == "ONE":
    price = price + 1.00
    Flag2 = Flag2 + 1

#Variations of 2
elif Toppings == "2":
    price = price + 1.75
    Flag2 = Flag2 + 1
elif CapsToppings == "TWO":
    price = price + 1.75
    Flag2 = Flag2 + 1

#Variations of 3
elif Toppings == "3":
    price = price + 2.50
    Flag2 = Flag2 + 1
elif CapsToppings == "THREE":
    price = price + 2.50
    Flag2 = Flag2 + 1

#Variations of 3
elif Toppings == "4":
    price = price + 3.35
    Flag2 = Flag2 + 1
elif CapsToppings == "FOUR":
    price = price + 3.35
    Flag2 = Flag2 + 1

#Size Valid Imput Check
if Flag2 == 0:
    print()
    print("Invalid Imput")

if Flag2 == 0:
    main()
#Calculation Pizza Price into Pizza Price + Tax
TaxPrice = (float(price)*0.13)
FinalPrice = (TaxPrice + price)

print()
print("This is your Subtotal: $",FinalPrice - TaxPrice)
print("This is your Tax: $",TaxPrice)
print("This is your Final Price: $", FinalPrice)