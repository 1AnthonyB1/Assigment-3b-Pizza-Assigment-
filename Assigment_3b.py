#Catilculaon for Size to Price

Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))

#Variations of Large
if Size == "Large":
    Price = 6.00
elif Size == "large":
    Price = 6.00

#Variations of Extra large
elif Size == "Extra Large":
     Price = 10.00
elif Size == "extra large":
     Price = 10.00
elif Size == "Extra large":
     Price = 10.00
elif Size == "extra Large":
     Price = 10.00
elif Size == "XL":
     Price = 10.00
elif Size == "xl":
     Price = 10.00
elif Size == "Xl":
     Price = 10.00
elif Size == "xL":
     Price = 10.00

#Calculation for Number's of toppings to Price

Toppings = (input("\nWhat Number of toppings do you want: \n 1,2, 3 or 4? \nType Number of Toppings:"))

#Variations of 1
if Toppings == "1":
    Price = Price + 1.00
elif Toppings == "One":
    Price = Price + 1.00
elif Toppings == "one":
    Price = Price + 1.00

#Variations of 2
elif Toppings == "2":
     Price = Price + 1.75 
elif Toppings == "Two":
     Price = Price + 1.75 
elif Toppings == "two":
     Price = Price + 1.75 

#Variations of 3
elif Toppings == "3":
     Price = Price + 2.50 
elif Toppings == "Three":
     Price = Price + 2.50 
elif Toppings == "three":
     Price = Price + 2.50 

#Variations of 4
elif Toppings == "4":
     Price = Price + 3.35 
elif Toppings == "Four":
     Price = Price + 3.35
elif Toppings == "four":
     Price = Price + 3.35 

#Calculation Pizza Price into Pizza Price + Tax

TaxPrice = (float(Price)*0.13)
FinalPrice = (TaxPrice+Price)

print()
print("This is your Subtotal:", FinalPrice - TaxPrice)
print("This is your Tax:",TaxPrice)
print("This is your Final Price:", FinalPrice)
