print("Jhonatan Roopnarine")
#The discounted price of an item after an employee and holiday discount
#Run the code for item price 169.96,1,048.96,47,25 with results 130.0194,802.4544,35.955,19.125
#Definiton of the function
def originalprice_to_saleprice(originalprice_float):
    #Declare employee discount
    employeediscount=originalprice_float*.15
    #Declare sale price 1 after employee discount
    saleprice1=originalprice_float-employeediscount
    #Declare holiday discount 
    holidaydiscount=saleprice1*.10
    #Declare sale price 2 after holiday discount
    saleprice2=saleprice1-holidaydiscount
    #Return the final sale price
    return(saleprice2)
#Prompt for the item price
ItemPrice=float(input("Enter the item price:"))
#Call the function
FinalPrice=originalprice_to_saleprice(ItemPrice)
#Print the final price
print("Final price after discounts:", FinalPrice)
#Print the original item price
print("Original item price:", ItemPrice)
