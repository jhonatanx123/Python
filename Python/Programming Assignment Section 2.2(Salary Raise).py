print("Jhonatan Roopnarine")
#Input salary of 3000 with any name and rating of 1, output should be "On probation"
#Input salary of 2000 with any name and rating of 2, output should be "Fair job, work harder and your new salary is: 2020"
#Input salary of 2500 with any name and rating of 3, output should be "Good job and your new salary is: 2550"
#Input salary of 4500 with any name and rating of 4, output should be "Very good and your new salary is: 4657.5"
#Input salary of 5650 with any name and rating of 5, output should be "Excellent job and your new salary is: 5932.5"

#Input employee's name
name=input("Enter employee's name:")
#Set newsalary to 0
newsalary=0
#Create a while loop
while name!="":
    #Take in the employee's current salary
    salary=input("Enter employee's current salary:")
    #Convert to float
    salary_float=float(salary)
    #Take in rating
    rating=input("Enter rating from 1-5:")
    #Convert to integer
    rating_int=int(rating)
    #Process program for if rating is from 1-5
    if rating_int==1:
        print("On probation")
    elif rating_int==2:
        newsalary=salary_float+(.01*salary_float)
        print("Fair job, work harder and your new salary is:", newsalary)
    elif rating_int==3:
        newsalary=salary_float+(.02*salary_float)
        print("Good job and your new salary is:", newsalary)
    elif rating_int==4:
        newsalary=salary_float+(.035*salary_float)
        print("Very good job and your new salary is:", newsalary)
    else: 
        newsalary=salary_float+(.05*salary_float)
        print("Excellent job and your new salary is:", newsalary) 
    #Start the loop again with the name
    name=input("Enter employee's name:")
    








