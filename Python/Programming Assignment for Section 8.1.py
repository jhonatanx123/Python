print("Jhonatan Roopnarine")
print()
#Test numbers 3,4,5 with output "This is a right triangle."
#Test numbers 6,8,10 with output "This is a right triangle."
#Test numbers 6,7,8 with output "This is not a right triangle."
#Test numbers 11,12,13 with output "This is not a right triangle."
#Define a function to test the situation
def rghtangtri(side1,side2,side3):
    #Test the case of the pythagorean theorem 
    if((side1*side1)+(side2*side2)==(side3*side3)):
        return True;
    else:
        return False;
    print()
#Ask the user to input each side 
side1 = int(input("Enter side1 of the triangle ="))
side2 = int(input("Enter side2 of the traingle ="))
side3 = int(input("Enter side3 of the triangle ="))
#Call the original funtion
result = rghtangtri(side1,side2,side3)
#Check the result and print a message depending on the situation
if(result == True):
    print("This is a right triangle.")
else:
    print("This is not a right triangle.")
        
