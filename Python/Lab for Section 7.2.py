#Test number 2 with output boy, car, truck, horse, crop, sold, bold, hello
#Test number 6 with output "No words longer than number."
#Test number 4 with output truck, horse, water, hello
print("Jhonatan Roopnarine")
print()
#Define a function
def listofWords(wordsList,number):
    if len(wordsList)>number:
        print(wordsList,end=" ")
        count=1
    else:
        count=0
    return count
#Declare the list
wordsList = ["boy","car","truck","horse","water","crop","sold","bold","hello"]
#Ask the user for a number(n) that will display words longer than that number
number = int(input("Enter a number to get words longer than it in the list:"))
#Print a statement for words longer than number 
print("Words longer than number:",end=" ")
count=0
#Create a for loop for no words longer than number
for x in wordsList:
    count+=listofWords(x,number)
if count==0:
    print()
    print("No words longer than number.")
    

