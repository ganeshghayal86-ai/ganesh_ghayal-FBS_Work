# Q6.WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

# take input

basic=int(input("enter basic_salry:"))

# perform operatin with formula
 
da=(basic*10)/100
ta=(basic*12)/100
hra=(basic*15)/100
total_salary=basic + da + ta + hra

# display result

print("DA is:",da)
print("TA is:",ta)
print("HRA is:",hra)
print("total salry of employee is:",total_salary)