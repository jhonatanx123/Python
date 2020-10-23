print("Jhonatan Roopnarine")
#Enter values 100,200,300,400,500 and code will end with sum of 1500 as it exceeds
#Enter 100,250,37,80,-50 and code will end with sum of 467
#Enter 2000 and code will end with sum of 2000 as it exceeds
#Enter -80 and code will end becasue there is no number to find the sum of 
#Set value to 0
sum=0
#Create a while loop to continue running the program until sum is equal to or greater than 1000
while sum<= 1000:
    #Input integer
    x=int(input("Enter an integer:"))
    #If x is a negative the program will print a message and end 
    if x<0:
        print("Invalid negative value given")
        break
    #Have the sum continue to increase  
    sum += x
#Print sum 
print("The sum is:",sum)
