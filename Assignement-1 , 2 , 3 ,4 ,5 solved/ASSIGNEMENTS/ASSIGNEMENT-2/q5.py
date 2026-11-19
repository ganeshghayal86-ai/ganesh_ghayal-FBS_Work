# Q5.WAP to calculate selling price of book based on cost price and discount.

# take input

cost_price=int(input("enter cost_price:"))
discount=int(input("enter discount:"))

# perform operation
# formula

discount=(cost_price*discount)/100
selling_price=cost_price-discount

# display result

print("discount:",discount)
print("selling_price:",selling_price)

