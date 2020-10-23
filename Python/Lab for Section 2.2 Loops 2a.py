print("Jhonatan Roopnarine")
#Enter 10 with output 55
#Enter 5 with output 15
#Enter 7 with output 28
#Get the input
a=input("Enter an ineteger number:")
#Convert to integer
a_int=int(a)
#Declare and initialize the variable
total_int=0
#Create a loop
for i in range(1,a_int+1):
    #Calculate the sum and store it
    total_int+=i
    #Check if "i" is less than "a_int"
    if i<a_int:
        #Print the consecutive integer
        print(i,end="+")
#Print the sum of the consecutive numbers
print(i,"=",total_int)
        
