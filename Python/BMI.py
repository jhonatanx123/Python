print("Jhonatan Roopnarine")
#Request a weight value from the user
weight=input("Enter weight to find BMI(in kg):")
#Request a height value from the user
height=input("Enetr height to find BMI(in meters):")
#Convert the weight into float type
weight_in_float=float(weight)
#Convert the height into float type
height_in_float=float(height)
#Calculate the BMI by dividing the value of weight_in_float by height_in_float
#Square height_in_float
BMI_val=weight_in_float/height_in_float**2
#Display the BMI value
print("BMI for the given height and weight is", BMI_val)
