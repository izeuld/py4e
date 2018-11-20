# asking user for input
inputhrs = input("Enter Hours:")
inputrate = input("Enter Rate:")
# "dangerous set of lines" - Dr Chuck
try:
    fhrs = float(inputhrs)
    frate = float(inputrate)
except:
    print("Error, only NUMERIC values allowed")
    quit()
# overtime and proper pay calculations
# as they depend on the "try" block, shouldn't they be inside it as well?
print(fhrs, frate)
if fhrs > 40:
    ovt = fhrs - 40
    pay = (frate * 40) + (frate * 1.5 * ovt)
else:
    pay = fhrs * frate
print(pay)
