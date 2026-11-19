# Q10.Write a program to reverse three-digit number.

# take input

num=int(input("enter number:"))

# perform opearation with formula

last = num % 10
middle = (num // 10) % 10
first = num // 100

reverse = last * 100 + middle * 10 + first

# display result

print("reverse three digit number is:",reverse)
