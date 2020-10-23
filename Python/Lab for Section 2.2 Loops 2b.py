print("Jhonatan Roopnarine")
#Get integer input
a=input("Enter an integer:")
#Convert to integer
a_int=int(a)
#Declare variable
total_int=0
#Create a loop
for n in range(1,a_int+1):
    total_int=0
#Create a loop
    for i in range(1,n+1):
        #Add i to total_int and store value
        total_int+=i
        #Check that i is less than n
        if i<n:
            #Print consecutive integer
            print(i,end="+")
    #Print sum of consecutive integer
    print(i,"=",total_int)
        
