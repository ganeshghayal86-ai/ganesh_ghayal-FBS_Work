# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

p1=int(input('enter price p1:'))
p2=int(input('enter price p2:'))
p3=int(input('enter price p3:'))
p4=int(input('enter price p4:'))
p5=int(input('enter price p5:'))

total=p1+p2+p3+p4+p5
GST=total*18/100
final_bill=total+GST
print('the total bill is:',final_bill)