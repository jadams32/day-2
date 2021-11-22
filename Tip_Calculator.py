# This is day 2 of the 100 days of code challange, here I create
#a tip calculator that displays how much each person should pay

# Welcome Statement
print("Welcome to The Tip Calculator!")

# Input amount for bill
total_bill = float(input("What is the total bill amount?\n$"))

# Input the percentage for the tip
tip_percent = int(input("Whats the percentage of tip that you would like to give?\n"))
# Input the amount of people to split the bill
total_people = int(input("How many people are splitting the bill?\n"))

# Perform calculations and rounding
bill_with_tip = total_bill * (1+(tip_percent/100))

amount_each_pays = round(bill_with_tip / total_people, 2)
amount_each_pays = "{:.2f}".format(amount_each_pays)

# Display the amount each person should pay
print(f"Each person will pay ${amount_each_pays}")
