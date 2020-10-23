print("Jhonatan Roopnarine")
#Test the the range [3,6] with range printed as 3 6 and sum as 18 and count as 4
#Set the sum to 0
sum=0
#Take the input from the user in the form of a number followed by a space with the other number
x,y=input("Enter a range of numbers:").split()
#Initialize the variables and chage them to integers 
x_int=int(x)
y_int=int(y)
#Set the count to 1 to include the starting number
count=1
#Create a for loop to compute the requirements 
for x in range(x_int,y_int+1):
    count+=1
    sum+=x
count-=1
#Print the required statements 
print("The range is:", x_int,y_int) 
print("The sum is:", sum)
print("The count is:", count)
