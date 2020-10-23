print("Jhonatan Roopnarine")
#The calculation of energy for the mass inputted
#Definition of the function
def energy_mass(mass_val):
    #Declare the variable light_speed constant
    light_speed=299792458
    #Return the energy
    return mass_val*light_speed**2
#Assign mass to variable mass
mass_str=input("Enter mass value in kilogram:")
#Convert the value in mass_str to integer
mass_int=int(mass_str)
#Function call energy_mass
energy=energy_mass(mass_int)
#Print the energy equivalent for mass
print("The energy equivalent for mass in meter-kilogram-second system is", energy)

               
