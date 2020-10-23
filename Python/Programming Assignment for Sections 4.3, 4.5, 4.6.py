print("Jhonatan Roopnarine")
#Password checker for password having at least 6 characters and at most 20//
#with at least one lowercase letter, one uppercase, and one number
#Get password from user
psw = input("Enter a password to be checked:")
#Initialize variables
valid = False
length = False
lowercase = False
uppercase = False
number = False
#Create if loop to check length 
if (len(psw)>=6 and len(psw)<=20):
    length = True
#Create for loop to check conditions
for char in psw:
    if(char.isupper()):
        uppercase = True
    if(char.isdigit()): 
        number = True   
    if(char.islower()): 
        lowercase = True    
#Check if all conditions are valid
if(lowercase and uppercase and number and length):
    valid = True
#Print statement depending on condition
if(valid):
    print("Password is valid.")
else:
    print("Password is invalid")
if length == False:
    print("Length is wrong.")
if lowercase == False:
    print("No lower case letters.")
if uppercase == False:
    print("No upper case letters.")
if number == False:
    print("No digits.")
    
