# Q7.Program to Find the Roots of a Quadratic Equation

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

# pehale use discrimanant formula

D = b**2 - 4*a*c

# use the root formula

x1=(-b+D**0.5) / (2*a)
x2=(-b-D**0.5) / (2*a)

# display result


print("x1 is:",x1)
print("x2 is:",x2)



