print("Jhonatan Roopnarine")
#Get the first input from user 
weight1=input("Enter weight in kg:")
#Convert to float
weight1_float=float(weight1)
#Use a while loop to end the code
while weight1_float>0:
    height1=input("Enter height in meters:")
    #Convert user input into float values
    height1_float=float(height1)
    #Calculate the BMI inputs of height and weight
    RESULT_BMI1=weight1_float/height1_float**2
    #Print the output of RESULT_BMI1
    print("Your first Body Mass Index is,",RESULT_BMI1)
    if RESULT_BMI1<18.5:
        #Display the weight status
        print("Based on CDC weight standard, your weight status is underweight")
    elif 18.5<=RESULT_BMI1<25:
        #Display the weight status
        print("Based on CDC weight standard, your weight status is normal")
    #Check whether the RESULT_BMI1 is between 25 and 30
    elif 25<=RESULT_BMI1<30:
        #Display the weight status
        print("Based on CDC weight standard, your weight status is overweight")
    #Check whether the RESULT_BMI1 is between 25 and 30
    else:
        #Display the weight status
        print("Based on CDC weight standard, your weight status is obese")                
    #Get the second inputs from user
    weight1=input("Enter weight in kg:")
    #Convert user input into a float value
    weight1_float=float(weight1)
  
