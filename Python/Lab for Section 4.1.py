print("Jhonatan Roopnarine")
#Input a word containing 5 characters
#Test Truck and Right
word=input("Enter a word that is 5 characters long:")
#Initialize the length of the word
length=len(word)
#Create a for loop for the rows and columns required to print the characters
for row in range(length):
    for col in range(row+1):
        print(word[col],end="")
    #Print the complete word
    print()
