print("Jhonatan Roopnarine")
#Get the first inputs from user 
weight1=input("Enter weight in kg:")
height1=input("Enter height in meters:")
#Convert user input into float values
weight1_float=float(weight1)
height1_float=float(height1)
#Calculate the BMI inputs of height and weight 
RESULT_BMI1=weight1_float/height1_float**2
#Print the output of RESULT_BMI1
print("Your first Body Mass Index is,",RESULT_BMI1)
#Get the second inputs from user
weight2=input("Enter weight in pounds:")
height2=input("Enter height in inches:")
#Convert user input into a float value
weight2_float=float(weight2)
height2_float=float(height2)
#Convert from kg and meters
height2_meters_float=height2_float*0.0254
weight2_Kg_float=weight2_float/2.2
#Calculate the BMI inputs of height and weight 
RESULT_BMI2=weight2_Kg_float/height2_meters_float**2
#Print the output of RESULT_BMI2
print("Your second Body Mass Index is, ",RESULT_BMI2)
#Check whether the RESULT_BMI1 less than 18.5
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
elif RESULT_BMI1>=30:
    #Display the weight status
    print("Based on CDC weight standard, your weight status is obese")
    
