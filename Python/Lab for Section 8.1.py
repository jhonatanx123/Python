print("Jhonatan Roopnarine")
#Test List1 with output [1,3,5,7,9]
#Set the list to List1
List1=[1,2,3,4,5,6,7,8,9]
#Define a function for removing the even numbers
def remove_even_numbers(List1):
    no_even_numbers=[]
    for x in List1:
        if x%2:
            no_even_numbers.append(x)
    #Print the results with the odd numbers only
    print(no_even_numbers)
    #Return the values in the list with the odds
    return no_even_numbers
#Call the function 
remove_even_numbers(List1)



#Test List2 with output [1,3,5,7,9]
List2=[1,2,3,4,5,6,7,8,9]
#Define a function for removing the odd numbers
def remove_odd_numbers(List2):
    no_odd_numbers=[]
    for x in List2:
        if x%2==0:
            no_odd_numbers.append(x)
    #Print the results with the even numbers only
    print(no_odd_numbers)
    #Return the values in the list with the evens
    return no_odd_numbers
#Call the function 
remove_odd_numbers(List2)
