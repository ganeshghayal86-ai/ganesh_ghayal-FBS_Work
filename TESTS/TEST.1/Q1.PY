length=int(input('enter length:'))
breadth=int(input('enter breadth:'))
radius=int(input('enter radius:'))


pi=3.14
area=(length*breadth)+(pi*radius**2/2)
perimeter=length+breadth+(2*radius)+(pi*radius)


print('area of given figure is:',area)
print('perimeter of given figure is:',perimeter)