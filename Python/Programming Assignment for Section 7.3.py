print("Jhonatan Roopnarine")
#L1=[1,3,5,5,2]
L1=[1,3,5,5,2];
#Sort the list
L1.sort();
print();
#Print the sorted list
print("After sorting list :",L1);
#Add 4 to the list 
L1.append(4);
#Print the list after appending 4
print("After appending 4 :",L1);
#Create a new list for removing the duplicate
newL1=[];
[newL1.append(each)for each in L1 if each not in newL1]
#Print the new list after removing the duplicate 
print("After removing duplicate :",newL1);
#Add 6 to anywhere in the list
newL1.insert(0,6);
#Print the items in the list and the number of items in the list
print("After inserting 6 in list :",newL1)
print("The number of items in the list :",len(newL1));
print(newL1)


