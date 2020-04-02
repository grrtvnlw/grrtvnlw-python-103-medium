# write a tip calculator based off user input and quality of service
# get user input for total bill amount, quality of service, and tip amount
total_bill = float(input("Total bill amount? "))
service_level = input("Level of service - good, fair, or bad? ")
tip = 0

if service_level == "good":
    tip = total_bill * .20
elif service_level == "fair":
    tip = total_bill * .15
elif service_level == "bad":
    tip = total_bill * .10

# format tip and bill to dollar amount
format_tip = '%.2f' % tip
total_bill += tip
format_total_bill = '%.2f' % total_bill

print(f"Tip amount: ${format_tip}")
print(f"Total amount: ${format_total_bill}")
