# Write a program to calculate profit or loss.
selling_price=int(input('enter selling price:'))
cost_price=int(input('enter cost price:'))

# loss=cost_price-selling_price
# profit=selling_price-cost_price

if selling_price>cost_price:
    print('profit')
elif cost_price>selling_price:
    print('loss')
else:
    print('no profit or loss')