# print multiplication table for numbers 1-10
# create initial values and set them equal to 1 because we don't want to multiply by 0
first_val = 1
second_val = 1

while first_val <= 10:
    result = first_val * second_val # declaring result variablie inside the first loop
    while second_val <= 10:
        print(f"{first_val} X {second_val} = {result}")
        second_val += 1
        result = first_val * second_val
    first_val += 1
    second_val = 0 # have to reset second_val to 0 so the second while loop starts again
    