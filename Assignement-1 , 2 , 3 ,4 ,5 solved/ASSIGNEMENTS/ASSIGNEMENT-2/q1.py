# 1. Convert the time entered in hh,min and sec into seconds.

# take input()

H=int(input("enter hours:"))
M=int(input("enter minutes:"))
S=int(input("enter seconds:"))

# first hours ko second main convert karo
hours_seconds=H*60*60

# second minuutes ko second main convert karo
minutes_seconds=M*60

sec=S

# total seconds ke liye

total_seconds=hours_seconds+minutes_seconds+sec

# display result

print("total_seconds is:",total_seconds)