print("Jhonatan, Kaitlyn, Maninder")
print("Welcome to Adelphi Hospital, how may we assist you today?")
#Create a class for the patient and initialize the values 
class Patient(object):
    #Define a function to accept information from the patient to use as the parameter
    def __init__(self,ID,name,sex,age,DOB,phone,address,height,weight,insurance):
        #Set the patient's credentials according to its field
        self.ID=ID
        self.name=name
        self.sex=sex
        self.age=age
        self.DOB=DOB
        self.phone=phone
        self.address=address
        self.height=height
        self.weight=weight
        self.insurance=insurance
    #Define a function to return the information taken in
    def __str__(self):
        return "ID:{}\nname:{}\nsex:{}\nage:{}\nDOB:{}\nheight:{}\nweight:{}\ninsurance:{}\naddress:{}\nphone:{}\n".format(self.ID,self.name,self.sex,self.age,self.DOB,self.height,self.weight,self.insurance,self.address,self.phone)
    #Create several functions to change the patient's information 
    def Update_address(self,address):
        self.address=address
    def Update_phone(self,phone):
        self.phone=phone
    def Update_weight(self,weight):
       self.weight=weight
#Create a while loop for entry of multiple patient's data.
Question = input("Do you have a patient to enter?:")
if Question == "Yes":
    ID=input("Enter patient's ID#:")
    name=input("Enter patient's name:")
    sex=input("Enter the patient's sex:")
    age=input("Enter the patient's age:")
    DOB=input("Enter the patient's DOB:")
    phone=input("Enter the patient's phone number:")
    address=input("Enter the patient's address:")
    height=input("Enter the patient's height:")
    weight=input("Enter the patient's weight:")
    insurance=input("Enter the patient's insurance:")
    print()
    p1=Patient(ID,name,sex,age,DOB,phone,address,height,weight,insurance)
    print(p1)
    #Ask the user if they want to update any information and ask them which field they want to update
    update_info = input("Do you want to update the patient's information?:")
    if update_info == "Yes":
        Answer = input("What field would you like to update?:")
        if Answer == "address":
            New_address = input("Enter the patient's new address:")
            p1.Update_address(New_address)
        if Answer == "phone":
            New_phone = input("Enter the patient's new phone number:")
            p1.Update_phone(New_phone)
        if Answer == "weight":
            New_weight = input("Enter the patient's new weight:")
            p1.Update_weight(New_weight)
        print(p1)
    Question = input("Do you have another patient to enter?:")
#Create another instance for patient two's entries
Question = input("Do you need to continue:")
if Question == "Yes":
    ID=input("Enter patient's ID#:")
    name=input("Enter patient's name:")
    sex=input("Enter the patient's sex:")
    age=input("Enter the patient's age:")
    DOB=input("Enter the patient's DOB:")
    phone=input("Enter the patient's phone number:")
    address=input("Enter the patient's address:")
    height=input("Enter the patient's height:")
    weight=input("Enter the patient's weight:")
    insurance=input("Enter the patient's insurance:")
    print()
    p2=Patient(ID,name,sex,age,DOB,phone,address,height,weight,insurance)
    print(p2)
    #Ask the user if they want to update any information and ask them which field they want to update
    update_info = input("Do you want to update the patient's information?:")
    if update_info == "Yes":
        Answer = input("What field would you like to update?:")
        if Answer == "address":
            New_address = input("Enter the patient's new address:")
            p2.Update_address(New_address)
        if Answer == "phone":
            New_phone = input("Enter the patient's new phone number:")
            p2.Update_phone(New_phone)
        if Answer == "weight":
            New_weight = input("Enter the patient's new weight:")
            p2.Update_weight(New_weight)
        print(p2)
    Question = input("Do you have another patient to enter?:")
#Create another instance for patient two's entries
Question = input("Do you need to continue:")
if Question == "Yes":
    ID=input("Enter patient's ID#:")
    name=input("Enter patient's name:")
    sex=input("Enter the patient's sex:")
    age=input("Enter the patient's age:")
    DOB=input("Enter the patient's DOB:")
    phone=input("Enter the patient's phone number:")
    address=input("Enter the patient's address:")
    height=input("Enter the patient's height:")
    weight=input("Enter the patient's weight:")
    insurance=input("Enter the patient's insurance:")
    print()
    p3=Patient(ID,name,sex,age,DOB,phone,address,height,weight,insurance)
    print(p3)
    #Ask the user if they want to update any information and ask them which field they want to update
    update_info = input("Do you want to update the patient's information?:")
    if update_info == "Yes":
        Answer = input("What field would you like to update?:")
        if Answer == "address":
            New_address = input("Enter the patient's new address:")
            p3.Update_address(New_address)
        if Answer == "phone":
            New_phone = input("Enter the patient's new phone number:")
            p3.Update_phone(New_phone)
        if Answer == "weight":
            New_weight = input("Enter the patient's new weight:")
            p3.Update_weight(New_weight)
        print(p3)
    Question = input("Do you have another patient to enter?:")
        
