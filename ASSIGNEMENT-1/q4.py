#4. Write a program to enter P, T, R and calculate simple Interest.

# take a valueS of P,T,R
# p=principal amount(initial money)
# t=time(in years)
# r=rate of interest per year
P=int(input("enter P:"))
R=int(input("enter R:"))
T=int(input("enter T:"))

# PERFORM OPEARATION OF SIMPLE INTEREST
SI=P*R*T/100


# DISPLAY RESULT
print("simple interest is:",SI)