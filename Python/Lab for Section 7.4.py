#Test phone with output "ehnop"
#Test Forty seven days till Christmas with output "     CFaadeehiillmnorrsssstttvyy"
#Test 47 days till Christmas with output "    47Caadhiillmrssstty"
#Test Santa will bring 5 presents and $20 dollars to house number #9110 for jenny. with output "            #$.0011259Saaabbdeeeeefghiijllmnnnnnnnoooprrrrssstttuuwy"
print("Jhontan Roopnarine")
#Define an original function string 
def string():
    #Take an input from the user
    string=list(input("Enter a string of characters :"))
    #Sort the list
    string.sort()
    #Print string
    print(string)
    #Convert the list back to a string
    string_new="".join(string)
    #Print the new string
    print(string_new)
#Call the function 
string()
