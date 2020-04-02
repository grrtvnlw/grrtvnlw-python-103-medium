# print a triangle 
# set a variable for icon, spaces, and counter
counter = 1 # have to set at 1 for initial icon to appear
icon = "*"
# spaces = " " * int((counter / 2))

while counter < 10:
    print(f"{spaces}{icon * counter}{spaces}")
    counter += 2