print("Jhonatan Roopnarine")
#The interest earned on a principal over a point of time
#Run the code for principal value 200, interest rate 3.5, and .5 years with output 3.5
#Run the code for principal value 1035, interest rate 2, and 2 years with output 41.4
#Run the code for principal value 10566.75, interest rate 5, and years 3 with output 1585.01
#Run the code for principal value 35675.86, interest rate 7.2, and 5.2 years with output 13357.04
#Definition of the function
def principal_to_interest(Principal,Rate,Time):
    #Declare interest
    interest=Principal*Rate*Time
    #Return the interest earned over time
    return(interest)
#Prompt for principal amount
Principal=float(input("What is the principal amount?:"))
#Prompt for the interest rate
Rate=float(input("What is the interest rate?:"))/100
#Prompt for the amount of time
Time=float(input("What is the amount of years?:"))
#Call the function
InterestEarned=principal_to_interest(Principal,Rate,Time)
#Print the interest earned 
print("Interest earned over time:", InterestEarned)
#Print the original principal amount
print("Original principal amount:", Principal)
#Print the interest rate
print("Interest rate:", Rate)
