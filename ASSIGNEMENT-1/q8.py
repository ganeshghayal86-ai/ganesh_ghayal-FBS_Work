# Q8.Write a program to convert days into years, weeks and days.

# take input()
days=int(input("enter total days:"))

# operation  perform years nikalne ke liye

years=days//365

# remaining days ke liye

remaining_days=days%365

# weeks nikalne ke liye

weeks=remaining_days//7

# weeks ke baad kitne remaining days hai iske liye

days=remaining_days % 7
# display result
print("years is:",years)
print("remaininig days is:",remaining_days)
print("weeks is:",weeks)
print("remaining days after weeks is:",days)