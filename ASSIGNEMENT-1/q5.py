# Write a program to enter P, T, R and calculate Compound Interest.
# take a values of p,t,r
p=int(input("enter p:"))
r=int(input("enter r:"))
t=int(input("enter t:"))

# perform operation with compound interest formula

A=p*(1+r/100)**t
CI=A-p

# display result
print("amount is:",A)
print("compound interest is:",CI)