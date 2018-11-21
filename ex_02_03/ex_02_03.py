# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hrs = input('Enter Hours:')
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)

pay = round((h * r), 2) # function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals
print('Pay:', pay)
