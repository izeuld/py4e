largest = None # largest value
smallest = None # smallest value

while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break # stop here, not later in code = exit mechanism
    try:
        intnum = int(num) # this part can be problematic, so needs to be put in a try/except
    except:
        print('Invalid input')
        continue # input was invalid, dont change num and tot, go back to start of while loop

    if intnum > largest:
        largest = intnum
    elif intnum < smallest:
        smallest = intnum

print("Maximum is", largest, "Minimum is", smallest)
