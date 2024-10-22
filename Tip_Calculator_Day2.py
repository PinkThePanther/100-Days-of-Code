print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage = bill * tip / 100

total = bill + percentage

split = total/people
rounded_split = round(split, 2)
rounded_total = round(total,2)
print(rounded_total)
print(rounded_split)

