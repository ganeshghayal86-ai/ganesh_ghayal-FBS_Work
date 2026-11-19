# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

total_percentage=0
students=int(input('enter students:'))
for i in range(1,students+1):
    total=0
    print('students:',i)
    
    for j in range(1,6):
        marks=int(input('enter marks of 5 sub::'))
        total+=marks
    percentage=(total/500)*100
    print('percentage is:',percentage)
    total_percentage+=percentage
average=total_percentage/students
print('average is:',average)







