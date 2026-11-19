# Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls./

length=int(input('enter length:'))
breadth=int(input('enter breadth:'))
rate=int(input('enter rate:'))
total_area=0
total_cost=0

area =length*breadth
total_area=4*length*breadth
total_cost=total_area*rate
print('total cost of painting is:',total_cost)
