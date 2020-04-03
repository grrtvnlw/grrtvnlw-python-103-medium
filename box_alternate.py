width = int(input("width? "))
height = int(input("height? "))

y = 0
while y < height:

    x = 0
    while x < width:
        is_top = (y == 0)
        is_bottom = (y == (height - 1))
        is_left = (x == 0)
        is_right = (x == (width - 1))

        if is_top or is_bottom or is_left or is_right:
            print('🔹', end='')
        else: 
            print('  ', end='')
        x = x + 1

    print()

    y = y + 1