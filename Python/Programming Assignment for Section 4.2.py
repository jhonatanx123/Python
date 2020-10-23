print("Jhonatan Roopnarine")
#Combine the two strings to get the alphabet in order from a-z in lowercase letters
#Declare the variables
x = "acegikmoqsuwy"
y = "bdfhjlnprtvxz"
z = ""
#Loop will execute until end of "x" variable
for i in range(len(x)):
    z = z + x[i] + y[i]
#Show z value
print(z)
