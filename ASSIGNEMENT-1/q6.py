#Q6.Write a Program to input two angles from user and find third angle of the triangle.

# take a values of angles1 and angle2
a1=int(input("enter angle1:"))
a2=int(input("enter angle2:"))

# perform operation of third angle
third_angle=180-a1-a2

# display result

print("third_angle of triangle is:",third_angle)
