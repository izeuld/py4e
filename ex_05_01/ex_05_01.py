# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# ups ^^' To stop a python script just press Ctrl + C

num = 0 # running count
tot = 0 # running total

while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break # exit mechanism = stop here, not later in code
    try:
        intval = int(sval) # this part can be problematic, so needs to be put in a try/except
    except:
        print('Invalid input')
        continue # input was invalid, dont change num and tot, go back to start of while loop
    print(intval) # prints last correct user-entered value
    num = num + 1
    tot = tot + intval

print('All done!')
print(num, tot, tot/num)
