print("Jhonatan Roopnarine")
print()
#Test (remove([1,2,3,4,5,6,7,8,9],True)) with result [2, 4, 6, 8]
#Test (remove([1,2,3,4,5,6,7,8,9],False)) with result [1, 3, 5, 7, 9] 
#Define a function to run the situation 
def remove(list,isOdd):
    #Set the result as an open list
    result=[]
    #Check each number in the list
    for num in list:
        #Test if the number is odd or even and append it to the list
        if num%2!=1 and isOdd:
            result.append(num)
        elif num%2!=0 and not isOdd:
            result.append(num)
    #Return the result to the list
    return result
#Print both situations when the odd or even is removed
print(remove([1,2,3,4,5,6,7,8,9],True))
print(remove([1,2,3,4,5,6,7,8,9],False))


