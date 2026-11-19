# Q9.Write a program to swap two numbers without using third variable.

# take input

a=int(input("enter a:"))
b=int(input("enter b:"))

# perform operation with formula

a=a+b
b=a-b
a=a-b

# display result

print("a is:",a)
print("b is:",b)
