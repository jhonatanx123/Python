print("Jhonatan Roopnarine")
#Take in the 1st and 2nd string and assign it to variables
str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
#Check the condition
if len(str1) < len(str2):
    print(str1, "is the smaller string.")
elif len(str2) < len(str1):
    print(str2, "is the smaller string.")
else:
    print("The strings have the same length.")

