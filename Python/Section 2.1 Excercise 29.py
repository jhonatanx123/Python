print("Jhonatan Roopnarine")
#Test numbers 25,307,92,135
#Import math
import math
#Get the input value from user
num=int(input('Enter an integer greater than 2:'))
#Declare and initialize the variable
counter=1
#Loop executes until the "num" is greater than "2"
while num>2:
    #Take the square root of number using sqrt() method
    num=math.sqrt(num)
    #Display the results of square root of number
    print(counter,":%f"%(num))
    #Increment the counter value by 1
    counter +=1
    
