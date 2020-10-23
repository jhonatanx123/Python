print("Jhonatan Roopnarine")
#Ask the user to enter a number or exit to end the program
each=input("Enter a number or exit to end the program:")
#Set a empty list for the numbers to append to
list=[]
#Create a while statement to run until the length equals 10
while len(list)<10:
    list.append(each)
    print(list)
    each=input("Enter a number:")
    #Create an if statement to end if exit is entered 
    if (each=="exit"):
        break
print(list)
