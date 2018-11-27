#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters: hours and rate

def computepay(hours, rate):
    hours = input('Enter Hours:')

    rate = input('Enter Rate:')
    try:
        fhours = float(hours)
        frate = float(rate)
    except:
        print('Provide a numeric value')
        # ?  why is it not allowed to put continue here?
    pay = fhours * frate
    print pay

computepay(10,2)
