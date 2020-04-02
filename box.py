# print a box based off user input for height and width
# create variables for user input for width and height
width = int(input("Width? "))
height = int(input("Height? "))

# adjust box dimensions based on user input
box_width = ("*" * width)
#have to offset width by 2 in order for dimensions to match
box_height = ("*" + (" " * (width - 2)) + "*\n") #add newline here instead of final format string
# display box
print(f"{box_width}\n{(box_height * (height - 2))}{box_width}") 