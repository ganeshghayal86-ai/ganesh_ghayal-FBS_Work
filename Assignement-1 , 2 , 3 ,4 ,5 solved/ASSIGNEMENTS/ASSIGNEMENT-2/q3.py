# 3. Convert distant given in feet and inches into meter and centimeter.

# take input

F=int(input("enter feet:"))
I=int(input("enter inches:"))

# convert feet into inches
feet_inches=F*12
# total inches
total_inches=feet_inches+I
# convert inches into centimeters
cm=total_inches*2.54

# Convert centimeters into meter and remaining centimeter
meter = int(cm // 100)
centimeter = cm % 100

# display result
print("meter=",meter)
print("centimeter=",centimeter)



