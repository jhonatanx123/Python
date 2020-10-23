print("Jhonatan Roopnarine")
#Enter -2 or any other number when there is no saved number and you will get a response of there is no input with sum of 0
#Enter 25 or any other number and then a negative and it should return the number as its average with sum of 25 or number that was entered
#Enter 10,30,50,8,7 or any other set of numbers followed by -2 or any other negative and code should end with average of 21 and sum of 105
#Enter 0 and output would be sum of 0 with average not being able to be calculated
#Create a lsit for the numbers
numbers=[]

#Set the number equal to 1
number=1
#Create a while loop for numbers greater than 0
while (number>0):
    #Take the input from the user
    number = int(input("Enter a number. Enter a negative to compute average:"))
    #Run the if statement for numbers greater than 0
    if number > 0:
        #save number for later use
        numbers.append(number)
#Print sum
print("The sum is:",sum(numbers))
#calculate average
if len(numbers)==0:
    print("You have not inputted anything, average cannot be calculated")
else:
    print("The average of your numbers is: %s" % (sum(numbers) / len(numbers)))

        
