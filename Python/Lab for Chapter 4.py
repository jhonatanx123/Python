print("Jhonatan Roopnarine")
#Get the user input
user_string = input("Enter a sentence:")
#Initialize variables
upper_case,lower_case,digits,punctuations = 0,0,0,0
#Create a loop condition and increment
for char in user_string:
    if char.islower():
        lower_case+=1
    elif char.isupper():
        upper_case+=1
    elif char.isdigit():
        digits+=1
    else:
        punctuations+=1
#Print the total for each variable
print("Uppercase:" +str(upper_case))
print("Lowercase:" +str(lower_case))
print("Digits:" +str(digits))
print("Punctuations:" +str(punctuations))
