#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None # container for largest value
smallest = None # container for smallest value

while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break # stop here, not later in code = exit mechanism
    try:
        intnum = int(num) # this part can be problematic, so needs to be put in a try/except
    except:
        print('Invalid input')
        continue # input was invalid, dont change num and tot, go back to start of the while loop

# ? does it matter whether the code below has two "ifs" or an "if" and "elif"?
    if largest is None or intnum > largest:
        largest = intnum
    elif smallest is None or intnum < smallest:
        smallest = intnum

print("Maximum is", largest)
print("Minimum is", smallest)
