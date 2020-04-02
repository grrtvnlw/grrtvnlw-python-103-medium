# write a tip calculator based off user input and quality of service and divide bill in equal parts
# get user input for total bill amount, quality of service, how many ways to split, and tip amount
total_bill = float(input("Total bill amount? "))
service_level = input("Level of service - good, fair, or bad? ")
split = float(input("Split how many ways? "))
tip = 0

# calculate tip based off user input
if service_level == "good":
    tip = total_bill * .20
elif service_level == "fair":
    tip = total_bill * .15
elif service_level == "bad":
    tip = total_bill * .10

# format tip, bill, and split bill to dollar amount and calculate total bill and split including tip
total_bill += tip
split_bill = total_bill / split

format_tip = '%.2f' % tip
format_total_bill = '%.2f' % total_bill
format_split_bill = '%.2f' % split_bill

# display formatted output
print(f"Tip amount: ${format_tip}")
print(f"Total amount: ${format_total_bill}")
print(f"Amount per person: ${format_split_bill}")
