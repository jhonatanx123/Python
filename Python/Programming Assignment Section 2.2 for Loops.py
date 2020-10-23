print("Jhonatan Roopnarine")
#Output should be 12 even and 12 odd
#Set values to 0 to start
count_odd=0
count_even=0
#Create the for loop with range 2-26 as 25 needs to be checked as well
for x in range(2,26):
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
#Print the number of even and odd numbers
print("Number of even numbers:", count_even)
print("Number of odd numbers:", count_odd)
