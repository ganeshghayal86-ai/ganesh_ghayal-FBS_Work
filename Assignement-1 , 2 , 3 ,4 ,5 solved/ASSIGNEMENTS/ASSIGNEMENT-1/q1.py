#1. Write a program to calculate the percentage of student based on marks of any 5 subjects

# take input
m1=int(input("enter mark sub1:"))
m2=int(input("enter mark sub2:"))
m3=int(input("enter mark sub3:"))
m4=int(input("enter mark sub4:"))
m5=int(input("enter mark sub5:"))

# perform addition of five subjects marks

obtained_marks=m1+m2+m3+m4+m5

# perform formula of percentahe  percentage = (obtained_marks/total_marks)*100

percentage=(obtained_marks/500)*100

# display result

print("obtained_marks:",obtained_marks)
print("percentage:",percentage)