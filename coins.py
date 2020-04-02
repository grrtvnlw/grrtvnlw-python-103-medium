# tally coin amount based on user input
# set initial coin value
coins = 0

#display initial coin value
print(f"You have {coins} coins.")

# get user input and store in variable inp
while True:
    inp = input("Do you want another? yes or no \n")
    if inp == "yes":
        coins += 1            
        print(f"You have {coins} coins.")
        continue # return to the start of the while loop and run it again
    elif inp == "no":
        print("Bye")
        break # exit the loop and program