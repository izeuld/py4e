# asking user for input
inputhrs = input("Enter Hours:")
inputrate = input("Enter Rate:")
# converting into floats
fhrs = float(inputhrs)
frate = float(inputrate)
# overtime and proper pay calculations
if fhrs > 40:
    ovt = fhrs - 40
    pay = (frate * 40) + (frate * 1.5 * ovt)
else:
    pay = fhrs * frate
print(pay)
