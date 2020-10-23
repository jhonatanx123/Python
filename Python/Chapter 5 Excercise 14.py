print("Jhonatan Roopnarine")
#Test value 5 and 10 outputs 5 and 10
#Test value 25 adds 3 and outputs 28
#Test value 50 adds 8 and outputs 58
#Test value 100 adds 20 and outputs 120
#Function definiton
def recharge(amount_int):
    #Check the amount_int is equal to 100
    if amount_int==100:
        #Add 20 to the amount_int
        amount_int+=20
    #Check the amount_int is equal to 50
    elif amount_int==50:
        #Add 8 to the amount_int
        amount_int+=8
    #Check the amount_int is equal to 25
    elif amount_int==25:
        #Add 3 to the amount_int
        amount_int+=3
    #Return statement
    return amount_int
#Function call
recharge_amount=input("Enter recharge amount($5,$10,$25,$50,$100):")
amount_int=int(recharge_amount)
while amount_int>0:
    amount=recharge(amount_int)
    #Print statement
    print("Total charge is",amount)
    recharge_amount=input("Enter recharge amount($5,$10,$25,$50,$100):")
    amount_int=int(recharge_amount)
    

                              
