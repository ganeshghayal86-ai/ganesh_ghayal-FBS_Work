
# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field. 



r=20
length=50
breadth=40
pi=3.14
wire=35
Circumference=2*pi*r
perimeter=2*(length*breadth)
totalperimeter=Circumference+perimeter

totalwire=totalperimeter*5
totalcost=totalwire*35

print(totalcost)