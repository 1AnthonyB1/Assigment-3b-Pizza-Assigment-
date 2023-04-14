#Calculations for Size to Price
def main():

    Size = (input("\nWhat Size of Pizza would you like: \nLarge? or Extra Large? \nType Size:"))
    Flag = 0

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
    elif Flag == 1:
        print()
        print(Price)
    if Flag == 0:
        main()
main()