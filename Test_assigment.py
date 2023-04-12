#Calculations for Size to Price
Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))

#Large Recignition & Price Calculation
CapsSize = str.upper(Size)
if CapsSize == "LARGE":
    Price = 6.00
elif CapsSize == "L":
    Price = 6.00


#Extra large Recignition & Price Calculation
elif CapsSize == "EXTRA LARGE":
    Price = 10.00
elif CapsSize == "XL":
    Price = 10.00

#Calculation for Number's of toppings to Price
Toppings = (input("\nWhat Number of toppings do you want: \n 1,2, 3 or 4? \nType Number of Toppings:"))


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
elif CapsToppings == "THREE":
    Price = Price + 3.35

#Calculation Pizza Price into Pizza Price + Tax

TaxPrice = (float(Price)*0.13)
FinalPrice = (TaxPrice+Price)

print()
print("This is your Subtotal: $",FinalPrice - TaxPrice)
print("This is your Tax: $",TaxPrice)
print("This is your Final Price: $", FinalPrice)
