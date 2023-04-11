#toppings = int(input(""))

Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))
if Size == "Large":
    Price = 6.00
elif Size == "Extra Large":
     Price = 10.00

Toppings = (input("\nWhat Number of toppings do you want: \n 1,2, 3 or 4? \nType Number of Toppings:"))
if Toppings == "1":
    Price = Price + 1.00
elif Toppings == "2":
     Price = Price + 1.75 
elif Toppings == "3":
     Price = Price + 2.50 
elif Toppings == "4":
     Price = Price + 3.35 
print(Price)